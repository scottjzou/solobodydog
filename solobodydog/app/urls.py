from django.conf.urls import url
from django.conf.urls import include, url
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^index/', views.index, name='index'),

    url(r'^$', views.index, name='index'),
    url(r'^users', views.users, name='users'),
    url(r'^login', views.login, name='login'),
    url(r'^profile', views.my_profile, name='my_profile'),
    url(r'^logout', views.logout, name='logout'),
    url(r'^signup', views.signup, name='signup'),


    # url('^', include('django.contrib.auth.urls')),
]

