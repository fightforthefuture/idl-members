from urlparse import urlparse
from django.utils.datastructures import MultiValueDictKeyError
from analytics.models import Impression
from campaigns.models import Campaign, Variant


def analytics_log(function):

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
