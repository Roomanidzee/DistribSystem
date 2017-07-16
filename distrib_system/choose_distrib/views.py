from django.contrib.auth.models import User
from django.shortcuts import render

from .models import Request, Container
from .utils import *
from django.contrib import messages
from userroles.views import base_context
    

# Create your views here.
'''
    Короче, сюда лезть только готовыми к дикой боли и дебаггингу))
'''
'''
STUDENTS HERE
'''


def student_form(request, user_id, container_type):
    user = request.user
    list_of_pairs = get_container_with_number_of_occupied_from_db(user, container_type)
    student_requests = get_requests_for_student(user, container_type.upper())
    context = {
        'user_id': user_id,
        'pairs': list_of_pairs,
        'requests': student_requests,
    }
    context.update(base_context(request))
    return render(request, 'accounts/parts/container_table.html', context)

# Ниже неотлаженный код
#########################


def student_make_request(request, user_id, container_type, container_id):
    user = user_id
    request = Request()
    request.student = user
    request.container = Container.objects.get(container_type=container_type, container_director=container_id)
    request.status = 0
    request.request_type = container_type
    request.save()


'''
PROFESSORS HERE
'''

def professor_form(request, user_id, request_type):
    user = request.user
    requests = list(Request.objects.filter(request_type=request_type, container=Container.objects.get(container_director=user)))
    context = {
        "requests": requests,
    }
    context.update(base_context(request))
    return render(request, 'accounts/parts/container_table.html', context)
    
def professor_request_change_status(request, user_id1, request_type, user_id2, status):
    user = request.user
    request = Request.objects.get(student=User.objects.get(user_id=user_id2), request_type=request_type, container=Container.objects.get(container_director=user))
    request.status = 1
    request.save()

'''
SCIENCE DIR HERE
'''


def sci_dir_form(request, user_id):
    user = request.user
    context = {}
    try:
        requests = list(Request.objects.filter(request_type='SCIENCE_HEAD', container=Container.objects.get(container_director=user)))
        context = {
            "requests": requests,
        }
    except:
        messages.add_message(request, messages.INFO, 'Список заявок пуст')
    context.update(base_context(request))
    return render(request, 'accounts/parts/container_table.html', context)

def sc_dir_request_change_status(request, user_id1, user_id2, request_status):
    user = request.user
    request = Request.objects.get(student=User.objects.get(user_id=user_id2), request_type='SCIENCE_HEAD', container=Container.objects.get(container_director=user))
    request.status = request_status
    request.save()

'''
COOPERATORS HERE
'''


def coop_form(request, user_id, request_type):
    user = request.user
    context = {}
    try:
        requests = list(Request.objects.filter(request_type=request_type, container=Container.objects.get(container_director=user)))
        context = {
            "requests": requests,
        }
    except:
        messages.add_message(request, messages.INFO, 'Список заявок пуст')
    context.update(base_context(request))
    return render(request, 'accounts/parts/container_table.html', context)




















