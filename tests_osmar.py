
# Create your tests here.
import xgboost
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','sampledeploy.settings')

import django
django.setup()

from sampleapp.models import Project

projects = Project.objects.all()

for project in projects:
    print(project)