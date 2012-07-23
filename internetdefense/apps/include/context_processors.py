from django.conf import settings


def include_url(request):
    return {
        'INCLUDE_URL': settings.INCLUDE_URL
    }
