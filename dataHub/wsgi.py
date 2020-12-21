import os
os.environ["DJANGO_SETTINGS_MODULE"] = "dataHub.settings"

from django.conf import settings
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

if not settings.DEBUG:
    try:
        application = get_wsgi_application()
    except:
        pass