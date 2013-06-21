from django.core.cache import cache
from django.core.management.base import BaseCommand
from django.db import connection

from analytics.queries import reach as reach_query
from analytics.settings import CACHE_KEY_REACH


class Command(BaseCommand):
    args = ''
    help = 'Calculates IDL network reach, sets value in cache'

    def handle(self, *args, **options):
        cursor = connection.cursor()
        cursor.execute(reach_query)
        reach_value = int(cursor.fetchall()[0][0])
        cache.set(CACHE_KEY_REACH, reach_value)