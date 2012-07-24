from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic.base import TemplateView

from campaigns.models import Campaign, Variant


class CustomizeView(TemplateView):
    """
    View for the page on which IDL members can configure the include code.
    """
    template_name = 'index.html'

    @method_decorator(cache_page(60 * 60 * 24 * 365))
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
