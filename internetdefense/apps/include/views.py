from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic.base import TemplateView

from campaigns.models import Campaign, Variant


class CustomizeView(TemplateView):

    template_name = 'index.html'

    @method_decorator(cache_page(60 * 60 * 24 * 365))
    def dispatch(self, *args, **kwargs):
        return super(CustomizeView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CustomizeView, self).get_context_data(**kwargs)
        context['campaigns'] = Campaign.objects.active()
        context['variants'] = Variant.objects.all()
        return context
