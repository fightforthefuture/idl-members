from urlparse import parse_qs, urlparse

from django.core.cache import cache
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic.base import TemplateView

from analytics.decorators import analytics_log
from campaigns.models import Campaign, Variant


class CustomizeView(TemplateView):
    """
    View for the page on which IDL members can configure the include code.
    """
    template_name = 'index.html'

    #@method_decorator(cache_page(60 * 60 * 24 * 365))
    def dispatch(self, *args, **kwargs):
        """
        Caches the view for 365 days.
        """
        return super(CustomizeView, self).dispatch(*args, **kwargs)
    
    def get_context_data(self, **kwargs):
        """
        Adds QuerySets of all active campaigns and presentational variants to
        the template context.
        """
        context = super(CustomizeView, self).get_context_data(**kwargs)
        context['campaigns'] = Campaign.objects.active()
        context['variants'] = Variant.objects.all()
        return context


class IncludeMixin(object):
    campaign = None
    test = None
    content_type = 'text/javascript'

    def render_to_response(self, context, **kwargs):
        """
        If available, returns a cached response. Otherwise, generates and
        caches a response.
        """
        gotten_response = self.get_response()
        if gotten_response:
            return gotten_response
        return self.create_response(context, **kwargs)

    def cache_key(self):
        """
        Creates a cache key, based on a hash of the context data (i.e. the
        configuration parameters passed by the implementors).
        """
        return '%s_%s' % (
            self.cache_key_prefix,
            hash(frozenset(self.settings().items())),
        )

    def create_response(self, context, **kwargs):
        """
        Creates and caches a response object based on the context data.
        """
        response = self.response_class(
            request=self.request,
            template=self.get_template_names(),
            context=context,
            **kwargs
        )
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

    def settings(self):
        return {
            'campaign': self.get_campaign(),
            'is_test': self.is_test(),
            'language_code': self.request.LANGUAGE_CODE,
            'variant': self.request.GET.get('variant', 'banner'),
            'country': self.request.session.get('country_name'),
            'url': '%s?%s' % (
                reverse('campaign'),
                self.request.META['QUERY_STRING'],
            ),
        }

    def get_campaign(self):
        """
        If campaign has already been determined in this view instance (i.e. in
        the same request/response cycle), return that.

        If a campaign is specified on the request (i.e. the implementor has
        explicitly requested to only display messages from a specific
        campaign), only return an active message from that campaign.

        Otherwise, return the latest active campaign, if there are any.
        """
        # For Project Megaphone
        return True
        
        if self.campaign is not None:
            return self.campaign

        slug = self.request.GET.get('campaign', None)

        
        if slug == 'NSA':
            slug = 'nsa'
        
        if slug:
            try:
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
        if self.test is None:
            querystring_test = self.request.GET.get('_idl_test', None) == '1'
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
        return self.settings()


class IframeView(IncludeMixin, TemplateView):
    cache_key_prefix = 'iframe'
    content_type = 'text/html'

    def get_template_names(self):
        slug = self.request.GET.get('campaign', None)
        campaign = self.get_campaign()
        if not campaign and slug:
            campaign = Campaign.objects.get(slug=slug)
        return campaign.template(self.settings()['variant'])


class IncludeView(IncludeMixin, TemplateView):
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
    template_name = 'include/js/include.js'
    context_data = None
    cache_key_prefix = 'js'
    content_type = 'application/x-javascript'

    @method_decorator(analytics_log)
    def dispatch(self, *args, **kwargs):
        """
        Default dispatch method, decorated to ensure that each request is
        logged.
        """
        return super(IncludeView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        """
        If there are no campaigns to display, return an empty response.
        Otherwise, set context data and return the appropriate response.
        """
        
        project_megaphone_is_active = True

        if not project_megaphone_is_active and not self.get_campaign() and not self.is_test():
            return HttpResponse()
        else:
            self.context_data = self.get_context_data(params=kwargs)
            return self.render_to_response(self.context_data, **kwargs)
