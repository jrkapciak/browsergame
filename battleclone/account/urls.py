from django.conf.urls import url, include
from . import views
from django.contrib import admin

urlpatterns = [
    url('^', include('django.contrib.auth.urls')),
    url(r'^signup/', views.RegistrationView.as_view(), name='signup'),
]