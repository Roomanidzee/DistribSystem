from django.conf.urls import url
from . import views

app_name = 'choose_distrib'
urlpatterns = [
    
    url(r'my_profile/(?P<user_id>[0-9]+)/student/practice', views.student_practice_form, name='student_practice'),
    url(r'my_profile/(?P<user_id>[0-9]+)/student/choice_course', views.student_course_form, name='student_choice_course'),
    url(r'my_profile/(?P<user_id>[0-9]+)/student/lab', views.student_lab, name='student_lab'),
    url(r'my_profile/(?P<user_id>[0-9]+)/student/sci_dir', views.student_sci_dir, name = 'student_sci_dir'),
    url(r'my_profile/(?P<user_id>[0-9]+)/student/practice/make_request/(?P<practice_id>[0-9]+)', views.student_practice_make_request, name='student_practice_make_request'),
    url(r'my_profile/(?P<user_id>[0-9]+)/student/choice_course/make_request/(?P<course_id>[0-9]+)', views.student_course_make_request, name='student_choice_course_make_request'),
    url(r'my_profile/(?P<user_id>[0-9]+)/student/lab/make_request/(?P<lab_id>[0-9]+)', views.student_lab_make_request, name='student_lab_make_request'),
    url(r'my_profile/(?P<user_id>[0-9]+)/student/sci_dir/make_request/(?P<sci_dir_id>[0-9]+)', views.student_sci_dir_make_request, name = 'student_sci_dir_make_request'),
    url(r'my_profile/(?P<user_id>[0-9]+)/professor/practice', views.professor_practice_form, name='professor_practice'),
    url(r'my_profile/(?P<user_id>[0-9]+)/professor/choice_course', views.professor_choice_course_form, name='professor_choice_course'),
    url(r'my_profile/(?P<user_id>[0-9]+)/professor/lab', views.professor_lab_form, name='professor_lab'),
    url(r'my_profile/(?P<user_id1>[0-9]+)/professor/practice/accept/(?P<user_id2>[0-9]+)', views.professor_practice_accept, name='professor_practice_accept'),
    url(r'my_profile/(?P<user_id1>[0-9]+)/professor/choice_course/accept/(?P<user_id2>[0-9]+)', views.professor_course_accept, name='professor_choice_course_accept'),
    url(r'my_profile/(?P<user_id1>[0-9]+)/professor/lab/accept/(?P<user_id2>[0-9]+)', views.professor_lab_accept, name='professor_lab_accept'),
    url(r'my_profile/(?P<user_id1>[0-9]+)/professor/practice/decline/(?P<user_id2>[0-9]+)', views.professor_practice_decline, name='professor_practice_decline'),
    url(r'my_profile/(?P<user_id1>[0-9]+)/professor/choice_course/decline/(?P<user_id2>[0-9]+)', views.professor_course_decline, name='professor_choice_course_decline'),
    url(r'my_profile/(?P<user_id1>[0-9]+)/professor/lab/decline/(?P<user_id2>[0-9]+)', views.professor_lab_decline, name='professor_lab_decline'),
    url(r'my_profile/(?P<user_id>[0-9]+)/sc_dir/sci_dir', views.sci_dir_form, name = 'sc_dir_sci_dir'),
    url(r'my_profile/(?P<user_id1>[0-9]+)/sc_dir/sci_dir/accept/(?P<user_id2>[0-9]+)', views.sci_dir_accept, name = 'sc_dir_sci_dir_accept'),
    url(r'my_profile/(?P<user_id1>[0-9]+)/sc_dir/sci_dir/decline/(?P<user_id2>[0-9]+)', views.sci_dir_decline, name = 'sc_dir_sci_dir_decline'),
    url(r'my_profile/(?P<user_id>[0-9]+)/cooperator/practice', views.coop_practice_form, name='cooperator_practice'),
    url(r'my_profile/(?P<user_id>[0-9]+)/cooperator/choice_course', views.coop_course_form, name='cooperator_choice_course'),
    url(r'my_profile/(?P<user_id>[0-9]+)/cooperator/lab', views.coop_lab_form, name='cooperator_lab'),
    url(r'my_profile/(?P<user_id>[0-9]+)/cooperator/sci_dir', views.coop_sci_dir_form, name = 'cooperator_sci_dir'),
    # url(r'my_profile/(?P<user_id1>[0-9]+)/print', views.print_version, name = 'print'),
    
]