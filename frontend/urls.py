from django.conf import settings
from django.conf.urls import url
from django.urls import *
from . import views
from django.conf.urls.static import static # new
from . import views
from django.contrib import admin


urlpatterns = [
    url(r'^react/$', views.index, name='react'),
    #path('api-auth/', include('rest_framework.urls')),
    #path('admin/', admin.site.urls),
]