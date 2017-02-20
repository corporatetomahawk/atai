from django.conf.urls import url

from . import views

urlpatterns = [
  url(r'^profile/$', views.profile, name='profile'),
  url(r'^table/$', views.simple_list, name='table'),
]