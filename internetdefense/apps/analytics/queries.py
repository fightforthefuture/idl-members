from django.conf import settings

engine = settings.DATABASES['default']['ENGINE']

if engine == 'django.db.backends.postgresql_psycopg2':
    reach = """
        SELECT AVG(daily_reach) FROM (
            SELECT   COUNT(DISTINCT ip) AS daily_reach,
                     date_part('day', time) AS day,
                     date_part('month', time) AS month,
                     date_part('year', time) AS year
            FROM     analytics_impression
            WHERE    time > (now() - interval '168 hour')
            GROUP BY year, month, day
        ) AS reach;
    """
    sites = """
        SELECT AVG(daily_reach) FROM (
            SELECT   COUNT(DISTINCT embedding_url) AS daily_reach,
                     date_part('day', time) AS day,
                     date_part('month', time) AS month,
                     date_part('year', time) AS year
            FROM     analytics_impression
            WHERE    time > (now() - interval '168 hour')
            GROUP BY year, month, day
        ) AS reach;
    """

else:
    sites = """
        SELECT AVG(daily_reach) FROM (
            SELECT   COUNT(DISTINCT embedding_url) as daily_reach,
                     strftime('%%d', time) AS day,
                     strftime('%%m', time) AS month,
                     strftime('%%Y', time) AS year
            FROM     analytics_impression
            WHERE    time > datetime('now', '-7 days')
            GROUP BY year, month, day
        );
    """
    reach = """
        SELECT AVG(daily_reach) FROM (
            SELECT   COUNT(DISTINCT ip) as daily_reach,
                     strftime('%%d', time) AS day,
                     strftime('%%m', time) AS month,
                     strftime('%%Y', time) AS year
            FROM     analytics_impression
            WHERE    time > datetime('now', '-7 days')
            GROUP BY year, month, day
        );
    """
