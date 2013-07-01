from django.conf import settings

CACHE_KEY_REACH = getattr(settings, 'ANALYTICS_CACHE_KEY_REACH', \
    'ANALYTICS_NETWORK_REACH')

CACHE_KEY_SITES = getattr(settings, 'ANALYTICS_CACHE_KEY_SITES', \
    'ANALYTICS_NETWORK_SITES')
