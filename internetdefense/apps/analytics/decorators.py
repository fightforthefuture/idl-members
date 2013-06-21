from urlparse import urlparse
from analytics.models import Impression
from campaigns.models import Campaign, Variant


def analytics_log(function):
    """
    Decorator which creates and saves an Impression instance each time the
    view is instantiated (i.e. once per response/request cycle). Can be
    directly applied to function-based views or applied as a method decorator
    to class-based views.

    Function based view example:

    @analytics_log
    def myview(request):
        return HttpResponse


    Class-based view example:

    class MyView(TemplateView):
        @method_decorator(analytics_log)
        def dispatch(self, *args, **kwargs):
            return super(MyView, self).dispatch(*args, **kwargs)
    """
    def wrapper(*args, **kw):
        request = args[0]
        impression = Impression()
        impression.ip = request.META['REMOTE_ADDR']
        try:
            referrer = request.META['HTTP_REFERER']
        except:
            pass
        else:
            impression.embedding_url = referrer
            impression.embedding_host = urlparse(referrer)[1]
        try:
            campaign = request.GET['campaign']
        except:
            campaign = None
        finally:
            if campaign:
                impression.campaign = Campaign.objects.get(slug=campaign)
            else:
                impression.campaign = Campaign.objects.latest() or None
                impression.is_autobroadcast = True
        try:
            variant = request.GET['variant']
        except:
            pass
        else:
            impression.variant = Variant.objects.get(slug=variant)
        try:
            impression.custom_url = request.GET['url']
        except:
            pass
        impression.save()
        return function(*args, **kw)

    return wrapper
