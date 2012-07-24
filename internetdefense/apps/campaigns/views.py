from urlparse import parse_qs, urlparse

from django.core.cache import cache
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from analytics.decorators import analytics_log

from campaigns.models import Campaign


class IncludeView(TemplateView):
    """
    A view to generate the IDL JavaScript

    Renders the JavaScript as a Django template, to ensure that only the
    necessary pieces are included. Additionally, to ensure the smallest
    possible payload, the results are minified in the template and are
    gzipped before transmission.

    If possible, response objects are cached based on a hash of the passed
    configuration, and the entire view is short-circuited by a comparison
    against this cache.
    """
    campaign = None
    template_name = 'include/js/include.js'
    context_data = None
    test = None

    @method_decorator(analytics_log)
    def dispatch(self, *args, **kwargs):
        """
        Default dispatch method, decorated to ensure that each request is
        logged.
        """
        return super(IncludeView, self).dispatch(*args, **kwargs)

    def cache_key(self):
        """
        Creates a cache key, based on a hash of the context data (i.e. the
        configuration parameters passed by the implementors).
        """
        return 'cached_js_%s' % hash(frozenset(self.context_data.items()))

    def create_response(self, context, **kwargs):
        """
        Creates and caches a response object based on the context data.
        """
        response = super(IncludeView, self).render_to_response(context,
            content_type='text/javascript', **kwargs)
        response.render()
        cache.set(self.cache_key(), response)
        return response

    def get_response(self):
        """
        Returns a cached response if one exists, otherwise returns None.
        """
        cached = cache.get(self.cache_key())
        if cached:
            return cached
        return None

    def render_to_response(self, context, **kwargs):
        """
        If available, returns a cached response. Otherwise, generates and
        caches a response.
        """
        gotten_response = self.get_response()
        if gotten_response:
            return gotten_response
        return self.create_response(context, **kwargs)

    def get(self, request, *args, **kwargs):
        """
        If there are no campaigns to display, return an empty response.
        Otherwise, set context data and return the appropriate response.
        """
        if not self.get_campaign() and not self.is_test():
            return HttpResponse()
        else:
            self.context_data = self.get_context_data(params=kwargs)
            return self.render_to_response(self.context_data, **kwargs)

    def get_campaign(self):
        """
        If campaign has already been determined in this view instance (i.e. in
        the same request/response cycle), return that.

        If a campaign is specified on the request (i.e. the implementor has
        explicitly requested to only display messages from a specific
        campaign), only return an active message from that campaign.

        Otherwise, return the latest active campaign, if there are any.
        """
        if self.campaign is not None:
            return self.campaign

        if 'campaign' in self.request.GET:
            try:
                slug = self.request.GET['campaign']
                self.campaign = Campaign.objects.active().get(slug=slug)
            except MultiValueDictKeyError:
                self.campaign = Campaign.objects.latest()
            except Campaign.DoesNotExist:
                self.campaign = Campaign.objects.none()
        else:
            self.campaign = Campaign.objects.latest()

        return self.campaign

    def is_test(self):
        """
        If this function has already been run in this view instance (i.e. in
        the same request/response cycle), return that.

        Returns a boolean indicating whether the IDL code is being tested
        (i.e. a test message should be returned). This is triggered in one of
        two ways:

        1) if the _idl_test querystring parameter is set to '1' on either the
        referring (i.e. embedding) page, or;
        2) in cases where that isn't possible, the same querystring parameter
        can be set as the URL of the include itself (i.e. of this view)
        """
        querystring_test = '_idl_test' in self.request.GET and '1' in \
            self.request.GET['_idl_test']
        if self.test is None:
            try:
                referer = urlparse(self.request.META['HTTP_REFERER'])
            except KeyError:
                self.test = querystring_test
            else:
                qs = parse_qs(referer[4])
                self.test = ('_idl_test' in qs and '1' in qs['_idl_test']) or \
                    querystring_test
        return self.test

    def get_context_data(self, **kwargs):
        """
        Set context data:
        - The campaign
        - The URL to include in the <iframe>
        - The presentational variant to use (e.g. modal, banner)
        """
        variant_name = self.request.GET['variant']
        campaign = self.get_campaign()
        try:
            template = self.request.GET['url']
        except MultiValueDictKeyError:
            template = campaign.template(variant_name) if campaign else None
        return {
            'campaign': campaign,
            'template': template,
            'variant': variant_name,
            'is_secure': self.request.is_secure(),
            'test': self.is_test()
        }
