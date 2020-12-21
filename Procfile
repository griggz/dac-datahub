release: python manage.py migrate
web: gunicorn unfData.wsgi:application
worker: celery -A unfData worker --concurrency 4
beat: celery -A unfData beat -S django