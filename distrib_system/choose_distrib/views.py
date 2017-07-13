from django.shortcuts import render_to_response
from django.template import RequestContext

from .utils import get_practice_from_db, get_course_from_db, get_lab_from_db, get_scidir_from_db

# Create your views here.

def practice_form(request, user_id):
    
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

def course_form(request, user_id):
    
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
    
    

def lab(request, user_id):
    
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

def sci_dir(request, user_id):
    
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

def practice_form_request(request, user_id):
    
    pass

def course_form_request(request, user_id):
    
    pass

def lab_request(request, user_id):
    
    pass

def sci_dir_request(request, user_id):
    
    pass

def accept(request, user_id1, user_id2):
    
    pass

def decline(request, uset_id1, user_id2):
    
    pass

def print_version(request, user_id):
    
    pass