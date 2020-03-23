from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('sampleapp.urls')),
    url(r'^', include('frontend.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('api/', include('articles.api.urls')),
    path('admin/', admin.site.urls),
    re_path(r'^.*', TemplateView.as_view(template_name='index.html')),
]
