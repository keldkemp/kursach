release: python manage.py migrate
web: gunicorn mysite.wsgi --env DJANGO_SETTINGS_MODULE=mysite.production --log-file -
