from urlparse import urlparse, urlunparse

from django.conf import settings


def secure_static_url(request):
    """
    Protocol-sensitive context processor that adds SECURE_STATIC_URL, which
    replaces the STATIC_URL protocol with https:// if the request was made
    with SSL.
    """
    static_url = list(urlparse(settings.STATIC_URL))
    if request.is_secure():
        static_url[0] = 'https'
    return {
        'SECURE_STATIC_URL': urlunparse(static_url)
    }


def include_domain(request):
    return {
        'INCLUDE_DOMAIN': settings.INCLUDE_DOMAIN
    }
