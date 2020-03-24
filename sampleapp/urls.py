from django.conf import settings
from django.conf.urls import url
from . import views
from django.conf.urls.static import static # new
from django.urls import path, include
from .views import (ProjectDetailView,
	ProjectListView,
	ProjectCreateView,
	ProjectDeleteView,
	ProjectUpdateView,)

urlpatterns = [

	path('list/projects/', ProjectListView.as_view()),
    path('project/<pk>', ProjectDetailView.as_view()),
    path('create_project/', ProjectCreateView.as_view()),
    path('delete_project/<pk>', ProjectDeleteView.as_view()),
    path('update_project/<pk>', ProjectUpdateView.as_view()),
	url(r'^home$', views.home, name='home'),
	url(r'^home2/$', views.home, name='home2'),
	url(r'^academic/$', views.academic, name='academic'),
	url(r'^contact/$', views.contact, name='contact'),
	url(r'^profesional/$', views.profesional, name='profesional'),
	url(r'^personal/$', views.personal, name='personal'),
	url(r'^predictive/$', views.predictive, name='predictive'),
	url(r'^algorithm/$', views.algorithm, name='algorithm'),
	url(r'^optimization/$', views.optimization, name='optimization'),
	url(r'^opinion/$', views.opinion, name='opinion'),
	url(r'^spatial/$', views.spatial, name='spatial'),
	url(r'^travel/$', views.travel, name='travel'),
	url(r'^places/$', views.places, name='places'),
	url(r'^album/$', views.album, name='album'),
	url(r'^machine/$', views.machine, name='machine'),
	url(r'^test/$', views.test, name='test'),
	url(r'^project_detail_2/(?P<pk>\d+)$', views.ProjectDetail.as_view(), name='project_detail'),
	url(r'^new_project/$', views.ProjectView.as_view(), name='new_project'),



]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)