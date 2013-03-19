from django.core.cache import cache
from django.core.management.base import BaseCommand
from django.db import connection

from analytics.queries import sites as sites_query
from analytics.settings import CACHE_KEY_SITES


class Command(BaseCommand):
    args = ''
    help = 'Calculates IDL network sites embedding the code, sets value in cache'

    def handle(self, *args, **options):
        cursor = connection.cursor()
        cursor.execute(sites_query)
        sites_value = int(cursor.fetchall()[0][0])
        cache.set(CACHE_KEY_SITES, sites_value)