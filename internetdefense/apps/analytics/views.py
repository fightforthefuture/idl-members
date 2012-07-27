from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import TemplateView


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
