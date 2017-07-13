from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import Request, Container
from .utils import get_practice_from_db, get_course_from_db, get_lab_from_db, get_scidir_from_db

from django.template.context_processors import request

# Create your views here.
'''
    Короче, сюда лезть только готовыми к дикой боли и дебаггингу))
'''
'''
STUDENTS HERE
'''
def student_practice_form(request, user_id):
    
    user = request.user
    
    practices_for_student = get_practice_from_db(user)
    
    context = {}
    
    i = 0
    
    for practice_item in practices_for_student:
        
        practice = {
            
            'container_name' : practice_item.container_name,
            'container_type' : practice_item.container_type,
            'container_director' : practice_item.container_director,
            'container_capacity' : practice_item.container_capacity
            
        }
        
        i += 1
        
        context['practice' + str(i)] = practice
        
    return render_to_response("distribution/my_profile" + str(user.id) + "/practice", context, context_instance=RequestContext(request))    

def student_course_form(request, user_id):
    
    user = request.user
    
    courses_for_student = get_course_from_db(user)
    
    context = {}
    
    i = 0
    
    for course_item in courses_for_student:
        
        course = {
            
            'container_name' : course_item.container_name,
            'container_type' : course_item.container_type,
            'container_director' : course_item.container_director,
            'container_capacity' : course_item.container_capacity
            
        }
        
        i += 1
        
        context['course' + str(i)] = course
        
    return render_to_response("distribution/my_profile" + str(user.id) + "/course", context, context_instance=RequestContext(request))    
    
    

def student_lab(request, user_id):
    
    user = request.user
    
    labs_for_student = get_lab_from_db(user)
    
    context = {}
    
    i = 0
    
    for lab_item in labs_for_student:
        
        lab = {
            
            'container_name' : lab_item.container_name,
            'container_type' : lab_item.container_type,
            'container_director' : lab_item.container_director,
            'container_capacity' : lab_item.container_capacity   
            
        }
        
        i += 1
        
        context['lab' + str(i)] = lab
        
    return render_to_response("distribution/my_profile" + str(user.id) + "/lab", context, context_instance=RequestContext(request))    

def student_sci_dir(request, user_id):
    
    user = request.user
    
    scidirs_for_student = get_scidir_from_db(user)
    
    context = {}
    
    i = 0
    
    for scidir_item in scidirs_for_student:
        
        sci_dir = {
            
            'container_name' : scidir_item.container_name,
            'container_type' : scidir_item.container_type,
            'container_director' : scidir_item.container_director,
            'container_capacity' : scidir_item.container_capacity
            
        }
        
        i += 1
        
        context['sci_dir' + str(i)] = sci_dir
        
    return render_to_response("distribution/my_profile" + str(user.id) + "/sci_dir", context, context_instance=RequestContext(request))    

def student_practice_make_request(request, user_id, practice_id):
    chosen_practice = practice_id
    user = user_id
    request = Request()
    request.student = user
    request.container = chosen_practice
    request.status = 0
    request.request_type = 'PRACTICE'
    request.save()
    

def student_course_make_request(request, user_id, course_id):
    chosen_practice = course_id
    user = user_id
    request = Request()
    request.student = user
    request.container = chosen_practice
    request.status = 0
    request.request_type = 'COURSE'
    request.save()
    

def student_lab_make_request(request, user_id, lab_id):
    chosen_practice = lab_id
    user = user_id
    request = Request()
    request.student = user
    request.container = chosen_practice
    request.status = 0
    request.request_type = 'LAB'
    request.save()


def student_sci_dir_make_request(request, user_id, sci_dir_id):
    chosen_practice = sci_dir_id
    user = user_id
    request = Request()
    request.student = user
    request.container = chosen_practice
    request.status = 0
    request.request_type = 'SCIENCE_HEAD'
    request.save()


'''
PROFESSORS HERE
'''

def professor_practice_form(request, user_id):
    pass


def professor_choice_course_form(request, user_id):
    pass


def professor_lab_form(request, user_id):
    pass


def professor_practice_accept(request, user_id1, user_id2):
    pass


def professor_course_accept(request, user_id1, user_id2):
    pass


def professor_lab_accept(request, user_id1, user_id2):
    pass


def professor_practice_decline(request, user_id1, user_id2):
    pass


def professor_course_decline(request, user_id1, user_id2):
    pass


def professor_lab_decline(request, user_id1, user_id2):
    pass

'''
SCIENCE DIR HERE
'''


def sci_dir_form(request, user_id):
    user = request.user
    requests = list(Request.objects.filter(request_type='SCIENCE_HEAD', container=Container.objects.get(container_director=user)))
    context = {
        "requests": requests,
    }
    return render_to_response("distribution/my_profile" + str(user.id) + "/requests", context, context_instance=RequestContext(request))

def sci_dir_accept(request, user_id1, user_id2):
    user = request.user
    request = Request.objects.get(student=User.objects.get(user_id=user_id2), request_type='SCIENCE_HEAD', container=Container.objects.get(container_director=user))
    request.status = 1
    request.save()

def sci_dir_decline(request, user_id1, user_id2):
    user = request.user
    request = Request.objects.get(student=User.objects.get(user_id=user_id2), request_type='SCIENCE_HEAD', container=Container.objects.get(container_director=user))
    request.status = 2
    request.save()

'''
COOPERATORS HERE
'''


def coop_practice_form(request, user_id):
    user = request.user
    requests = list(Request.objects.filter(request_type='PRACTICE'))
    context = {
        "requests": requests
    }
    return render_to_response("distribution/my_profile" + str(user.id) + "/practice", context, context_instance=RequestContext(request))

def coop_course_form(request, user_id):
    user = request.user
    requests = list(Request.objects.filter(request_type='COURSE'))
    context = {
        "requests": requests
    }
    return render_to_response("distribution/my_profile" + str(user.id) + "/choice_course", context, context_instance=RequestContext(request))

def coop_lab_form(request, user_id):
    user = request.user
    requests = list(Request.objects.filter(request_type='LAB'))
    context = {
        "requests": requests
    }
    return render_to_response("distribution/my_profile" + str(user.id) + "/lab", context, context_instance=RequestContext(request))

def coop_sci_dir_form(request, user_id):
    user = request.user
    requests = list(Request.objects.filter(request_type='SCIENCE_HEAD'))
    context = {
        "requests": requests
    }
    return render_to_response("distribution/my_profile" + str(user.id) + "/sci_dir", context, context_instance=RequestContext(request))




















