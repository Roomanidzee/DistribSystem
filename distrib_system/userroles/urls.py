from django.conf.urls import url
from .views import register

urlpatterns = [
    url(r'^register/$', register, name='register'),
    #url(r'^login/$', 'django.contrib.auth.views.login', { "template_name": "login.html" }),
    #url(r'^logout/$', 'django.contrib.auth.views.logout_then_login'), 
]
