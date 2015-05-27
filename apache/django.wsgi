import os
import sys
sys.path.append('d:/stockdiary')
os.environ['DJANGO_SETTINGS_MODULE']='stockdiary.settings'

#import django.core.handlers.wsgi
#application=django.core.handlers.wsgi.WSGIHandler()

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()