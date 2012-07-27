web: newrelic-admin run-program python manage.py run_gunicorn -b 0.0.0.0:$PORT -w 9 -k gevent
celeryd: python manage.py celeryd -E --loglevel=INFO
