from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url('^', include('django.contrib.auth.urls'))
]