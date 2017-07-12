from django.conf.urls import url
from django.contrib.auth import views as djangoviews
from . import views

app_name = 'userroles'
urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', djangoviews.login, {"template_name": "login.html"}),
    url(r'^logout/$', djangoviews.logout_then_login),
    url(r'^my_profile/(?P<user_id>[0-9]+)/$', views.my_profile, name='profile'),
    url(r'^my_profile/(?P<user_id>[0-9]+)/editprof/$', views.edit_profile, name='edit_profile'),
    url(r'^my_profile/(?P<user_id>[0-9]+)/editpass/$', views.edit_password, name='edit_password'),
]
