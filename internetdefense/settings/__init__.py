from os import environ, path, pardir
import socket
from sys import path as pythonpath

APP_DIR = path.normpath(path.join(path.dirname(__file__), pardir))
PROJECT_DIR = path.normpath(path.join(APP_DIR, pardir))

# Add project and apps directories to PYTHONPATH for cleaner imports
pythonpath.insert(1, path.join(APP_DIR))
pythonpath.insert(2, path.join(APP_DIR, 'apps'))

# Import base settings
base = __import__('settings.base', {}, {}, ['base'], -1)
for setting in dir(base):
    if setting == setting.upper():
        locals().update({setting: getattr(base, setting)})

environments = {}

# Allow environment to be defined by either environment variable (set in, e.g.,
# a WSGI script) or via hostname.
wsgi_env = environ.get('WSGI_ENVIRONMENT', None)
env_name = wsgi_env or getattr(environments, socket.gethostname(), 'dev')

# Import environment settings
try:
    environment_settings = __import__('settings.%s' % env_name, globals(),
        locals(), [env_name], -1)
except ImportError:
    pass
else:
    for setting in dir(environment_settings):
        if setting == setting.upper():
            locals().update({setting: getattr(environment_settings, setting)})
