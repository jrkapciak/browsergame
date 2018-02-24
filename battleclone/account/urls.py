from django.conf.urls import url, include
from . import views
from django.contrib import admin

urlpatterns = [
    url('^', include('django.contrib.auth.urls')),
    url('^singup/$', views.signup, name='signup'),
]