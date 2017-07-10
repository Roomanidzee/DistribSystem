from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', 'django.contrib.auth.views.login', { "template_name": "accounts/login.html" }),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login'), 
]
