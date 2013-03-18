"""
Settings specific to the production environment.
"""

import os

from memcacheify import memcacheify
from postgresify import postgresify

from settings.base import INSTALLED_APPS


DEBUG = True
TEMPLATE_DEBUG = DEBUG

SITE_ID = 2

INSTALLED_APPS = INSTALLED_APPS + [
    'gunicorn',
]

DATABASES = postgresify()
CACHES = memcacheify()

SECRET_KEY = os.environ.get('SECRET_KEY')

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = 'internetdefenseleague'
AWS_QUERYSTRING_AUTH = False
AWS_HEADERS = {
    'Cache-Control': 'max-age=2592000',
}

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https',)

STATIC_URL = 'http://internetdefenseleague.s3.amazonaws.com/'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
COMPRESS_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

COMPRESS_OFFLINE_CONTEXT = {
    'SECURE_STATIC_URL': 'https://internetdefenseleague.s3.amazonaws.com',
}
INCLUDE_DOMAIN = 'members.internetdefenseleague.org'
INCLUDE_URL = INCLUDE_DOMAIN + '/include/'
