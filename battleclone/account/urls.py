from django.conf.urls import url, include
from . import views

urlpatterns = [
    url('^', include('django.contrib.auth.urls')),

    url(r'^signup/', views.RegistrationView.as_view(), name='signup'),

    url(r'^profile/(?P<pk>\d+)/edit',
        views.EditProfileView.as_view(),
        name='edit_profile'),
]