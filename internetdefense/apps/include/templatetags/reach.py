from django import template
from django.db import connection

from analytics.queries import reach as reach_query

register = template.Library()


@register.inclusion_tag('include/reach_tag.html')
def reach():
    cursor = connection.cursor()
    cursor.execute(reach_query)
    return {
        'reach': int(cursor.fetchall()[0][0])
    }
