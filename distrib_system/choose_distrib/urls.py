from django.conf.urls import url
from . import views

urlpatterns = [
    
    url(r'my_profile/(?P<user_id>[0-9]+)/practice', views.practice_form, name='practice'),
    url(r'my_profile/(?P<user_id>[0-9]+)/choice_course', views.course_form, name='choice_course'),
    url(r'my_profile/(?P<user_id>[0-9]+)/lab', views.lab, name='lab'),
    url(r'my_profile/(?P<user_id>[0-9]+)/sci_dir', views.sci_dir, name = 'sci_dir'),
    url(r'my_profile/(?P<user_id>[0-9]+)/practice/request', views.practice_form_request, name='practice_request'),
    url(r'my_profile/(?P<user_id>[0-9]+)/choice_course/request', views.course_form_request, name='choice_course_request'),
    url(r'my_profile/(?P<user_id>[0-9]+)/lab/request', views.lab_request, name='lab_request'),
    url(r'my_profile/(?P<user_id>[0-9]+)/sci_dir/request', views.sci_dir_request, name = 'sci_dir_request'),
    url(r'my_profile/(?P<user_id1>[0-9]+)/accept/(?P<user_id2>[0-9]+)', views.accept, name = 'accept'),
    url(r'my_profile/(?P<user_id1>[0-9]+)/decline/(?P<user_id2>[0-9]+)', views.decline, name = 'decline'),
    url(r'my_profile/(?P<user_id1>[0-9]+)/print', views.print_version, name = 'print'),
    
]