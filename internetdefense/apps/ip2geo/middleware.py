# -*- coding: utf-8 -*-
#from django.conf import settings
from django.conf import settings
from django.utils.encoding import smart_unicode as _
from ip2geo import pygeoip
from ip2geo.pygeoip.util import long2ip

import re

# this is not intended to be an all-knowing IP address regex
IP_RE = re.compile('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')

def get_ip(request):
    """
    Method of django-tracking plugin
    
    Retrieves the remote IP address from the request data.  If the user is
    behind a proxy, they may have a comma-separated list of IP addresses, so
    we need to account for that.  In such a case, only the first IP in the
    list will be retrieved.  Also, some hosts that use a proxy will put the
    REMOTE_ADDR into HTTP_X_FORWARDED_FOR.  This will handle pulling back the
    IP from the proper place.
    """

    # if neither header contain a value, just use local loopback
    ip_address = request.META.get('HTTP_X_FORWARDED_FOR',
                                  request.META.get('REMOTE_ADDR', '127.0.0.1'))
    if ip_address:
        # make sure we have one and only one IP
        try:
            ip_address = IP_RE.match(ip_address).group(0)
        except IndexError:
            pass

    return ip_address

GEOIP_UNKNOWN = _('')

class CityMiddleware(object):
    """
    More information about Python-MaxMind: http://code.google.com/p/pygeoip/
    
    In settings.py: 
    
    GEOIP_DATA = '/path/to/GeoLiteCity.dat'
    
    You can choose the following fields that will be stored in the session: 
    GEOIP_SESSION_FIELDS = ['country_name', 'country_code', 'country_code3', 'region_name', 'city', 'latitude', 'longitude', 'postal_code']
    
    You do not have to select all of them, for example:
    GEOIP_SESSION_FIELDS = ['country_name', 'region_name', 'city',]
    
    PS1: The data is responsability of MaxMind database.
    PS2: The documentation of each field you can find in MaxMind reference.
    PS3: The field 'geoip' is set to True in session to identify that the data was loaded
    """
    
    def __init__(self):
        super(CityMiddleware, self).__init__()
        self.gip = pygeoip.GeoIP(settings.GEOIP_DATA, pygeoip.MEMORY_CACHE)
    
    def process_view(self, request, view_func, *view_args, **view_kwargs):
        if not 'geoip' in request.session:
            try:
                ip = get_ip(request)

                # For local testing
                if ip == '127.0.0.1':
                    ip = '96.41.253.160'

                record = self.gip.record_by_addr(ip)
                for field in settings.GEOIP_SESSION_FIELDS:
                    try:
                        request.session[field] = _(record[field], encoding='iso8859-1', strings_only=False)
                    except:
                        request.session[field] = GEOIP_UNKNOWN
            except Exception, e:
                for field in settings.GEOIP_SESSION_FIELDS:
                    request.session[field] = GEOIP_UNKNOWN
            request.session['geoip'] = True
        return None
            
