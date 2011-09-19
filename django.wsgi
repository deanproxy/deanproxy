import os, sys
path = os.path.dirname(os.path.realpath(__file__))

if path not in sys.path:
	sys.path.append(path)

os.environ['DJANGO_RUN_ENV'] = 'production'
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

