from django.core.cache import cache
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import TemplateView

from analytics.settings import CACHE_KEY_REACH


class ReachView(TemplateView):
    """
    Shows an HTML5 <meter> element displaying the overall reach of the IDL
    against a progress bar, intended to be pulled in via Ajax.
    """
    template_name = 'reach.html'

    @method_decorator(cache_page(60 * 60 * 24))
    def dispatch(self, *args, **kwargs):
        """
        Caches the view for 24 hours.
        """
        return super(ReachView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        """
        Adds QuerySets of all active campaigns and presentational variants to
        the template context.
        """
        context = super(ReachView, self).get_context_data(**kwargs)
        context['reach'] = cache.get(CACHE_KEY_REACH)
        return context
