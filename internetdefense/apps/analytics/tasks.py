from celery import task

from django.core.cache import cache
from django.db import connection

from analytics.queries import reach as reach_query
from analytics.settings import CACHE_KEY_REACH


@task()
def reach():
    """
    Calculate IDL network's reach, add calculated value to cache for templates
    """
    cursor = connection.cursor()
    cursor.execute(reach_query)
    cache.set(CACHE_KEY_REACH, int(cursor.fetchall()[0][0]))
