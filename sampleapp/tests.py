import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','sampledeploy.settings')

import django
django.setup()
from sampleapp.models import *

projects = Projects.objects.all().delete()