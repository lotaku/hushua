from django.conf.urls import patterns, url
from hs_info import views

urlpatterns = patterns('',

	url(r'^index/$', views.index, name='index'),
	url(r'^add_task/$', views.add_task, name='add_task'),
)