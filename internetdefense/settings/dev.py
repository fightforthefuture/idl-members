"""
Settings specific to development environments
"""

from os import path

from settings.base import PROJECT_DIR, MIDDLEWARE_CLASSES, INSTALLED_APPS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': path.join(PROJECT_DIR, 'data.db'),
    }
}

DEBUG = True
TEMPLATE_DEBUG = True

SITE_ID = 1

INCLUDE_URL = '127.0.0.1:8000/include/'
STATIC_URL = '/static/'


def show_toolbar(request):
    return True

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TOOLBAR_CALLBACK': show_toolbar,
}
INTERNAL_IPS = ('127.0.0.1',)
MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES + [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]
INSTALLED_APPS = INSTALLED_APPS + [
    'debug_toolbar',
]

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': path.join(PROJECT_DIR, 'cache'),
        'TIMEOUT': 60 * 60 * 24 * 365
    }
}
