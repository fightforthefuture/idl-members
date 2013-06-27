from django.core.cache import cache
from django.core.management import call_command
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import TemplateView

from analytics.settings import CACHE_KEY_REACH, CACHE_KEY_SITES


class ReachView(TemplateView):
    """
    Shows an HTML5 <meter> element displaying the overall reach of the IDL
    against a progress bar, intended to be pulled in via Ajax.
    """
    template_name = 'reach.html'

    #@method_decorator(cache_page(60 * 60 * 24))
    def dispatch(self, *args, **kwargs):
        """
        Caches the view for 24 hours.
        """
        return super(ReachView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        """
        Adds IDL network reach to context, forcing the number to be calculated
        if it isn't already in cache.
        """
        context = super(ReachView, self).get_context_data(**kwargs)
        reach = cache.get(CACHE_KEY_REACH)
        sites = cache.get(CACHE_KEY_SITES)
        if not sites:
            call_command("get_sites")
            sites = cache.get(CACHE_KEY_SITES) or NONE
        if not reach:
            call_command('get_reach')
            reach = cache.get(CACHE_KEY_REACH) or None
        context['reach'] = reach
        context['sites'] = sites
        context['progress'] = int(85000 / 3500)  # Goal of 350K, as a percent
        return context

    def render_to_response(self, context, **response_kwargs):
        """
        Adds CORS headers to response
        """
        response = super(ReachView, self).render_to_response(context, \
            **response_kwargs)
        response['Access-Control-Allow-Origin'] = '*'
        return response
