release: python manage.py migrate --noinput
web: gunicorn mysite.wsgi --env DJANGO_SETTINGS_MODULE=mysite.production --log-file -
