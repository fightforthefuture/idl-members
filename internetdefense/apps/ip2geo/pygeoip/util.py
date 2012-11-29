"""
Misc. utility functions. It is part of the pygeoip package.

@author: Jennifer Ennis <zaylea at gmail dot com>

@license:
Copyright(C) 2004 MaxMind LLC

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/lgpl.txt>.
"""

def ip2long(ip):
    """
    Convert a IPv4 address into a 32-bit integer.
    
    @param ip: quad-dotted IPv4 address
    @type ip: str
    @return: network byte order 32-bit integer
    @rtype: int
    """
    ip_array = ip.split('.')
    ip_long = long(ip_array[0]) * 16777216 + long(ip_array[1]) * 65536 + long(ip_array[2]) * 256 + long(ip_array[3])
    return ip_long  

def long2ip(slong):
    """
    Convert a 64-bit long to a IPv4 address
    
    @param: network byte order 64-bit long
    @type: long
    @return ip: quad-dotted IPv4 address
    @rtype ip: str '[0-255].[0-255].[0-255].[0-255]'
    """
    nlong = long(slong)
    one = nlong / 16777216
    optmizing = nlong % 16777216
    two = optmizing / 65536
    optmizing = optmizing % 65536
    three = optmizing / 256
    four = optmizing % 256
    return '%s.%s.%s.%s' % (str(one), str(two), str(three), str(four))

