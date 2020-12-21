release: python manage.py migrate
web: gunicorn dataHub.wsgi:application
worker: celery -A dataHub worker --concurrency 4
beat: celery -A dataHub beat -S django