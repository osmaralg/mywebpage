from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
#from rest_auth.registration.views import VerifyEmailView, RegisterView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('sampleapp.urls')),
    #path('api-auth/', include('rest_framework.urls')),
    #path('rest-auth/', include('rest_auth.urls')),
    #path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('api/', include('articles.api.urls')),
    re_path(r'^.*', TemplateView.as_view(template_name='index.html')),
	#path('registration/', include('rest_auth.registration.urls')),
	#path('registration/', RegisterView.as_view(), name='account_signup'),
	#re_path(r'^account-confirm-email/', VerifyEmailView.as_view(),
	#     name='account_email_verification_sent'),
	#re_path(r'^account-confirm-email/(?P<key>[-:\w]+)/$', VerifyEmailView.as_view(),
	#     name='account_confirm_email'),
	#url(r'^', include('django.contrib.auth.urls')),
]
