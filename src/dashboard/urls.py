from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views
from . import matches_view


urlpatterns = [
    url(r'^portfolio/(?P<portfolio_id>[0-9]+)/$', views.portfolio_view, name='portfolio'),
    url(r'^$', views.dashboard, name='dashboard'),
]
