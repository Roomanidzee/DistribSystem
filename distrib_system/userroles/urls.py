from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', 'django.contrib.auth.views.login', { "template_name": "accounts/login.html" }),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login'),
    url(r'^my_profile/(?P<user_id>[0-9]+)/$', views.my_profile, name='profile'),
    url(r'^my_profile/(?P<user_id>[0-9]+)/editprof/$', views.edit_profile, name='edit_profile'),
    url(r'^my_profile/(?P<user_id>[0-9]+)/editpass/$', views.edit_password, name='edit_password'),
]
