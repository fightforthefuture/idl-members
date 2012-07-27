"""
Base settings that are applied to each environment, before overriding with any
environment-specific settings.
"""

from os import pardir, path

# Path settings
APP_DIR = path.normpath(path.join(path.dirname(__file__), pardir))
PROJECT_DIR = path.normpath(path.join(APP_DIR, pardir))

STATIC_ROOT = path.join(APP_DIR, 'collected_static')
STATIC_URL = '/static/'
STATICFILES_DIRS = (path.join(APP_DIR, 'static'),)
MEDIA_ROOT = path.join(APP_DIR, 'media')
MEDIA_URL = '/media/'
TEMPLATE_DIRS = (
    path.join(APP_DIR, 'templates'),
)
FIXTURE_DIRS = (
    path.join(APP_DIR, 'fixtures'),
)


# Debugging settings
DEBUG = False
TEMPLATE_DEBUG = DEBUG
ADMINS = (
    ('Chuck Harmston', 'fftf@chuckharmston.com'),
)
MANAGERS = ADMINS


# Localization settings
TIME_ZONE = 'America/New_York'
USE_I18N = True
USE_L10N = True
LANGUAGE_CODE = 'en-us'


# Apps, classes, processors, and loaders
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]
TEMPLATE_LOADERS = [
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
]
MIDDLEWARE_CLASSES = [
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]
INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'kombu.transport.django',
    'djcelery',
    'south',
    'campaigns',
    'analytics',
    'include',
]
TEMPLATE_CONTEXT_PROCESSORS = [
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    'include.context_processors.include_url',
    'internetdefense.context_processors.secure_static_url',
]


# Misc. settings
SECRET_KEY = 'dskba^j4%zysn*d-+yh!w!2_vd938d2pia0dk0v40yie^t!tc$'
ROOT_URLCONF = 'urls'
INTERNAL_IPS = ('127.0.0.1',)
MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'
BROKER_BACKEND = 'django'
