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
    list_of_triples = get_container_with_number_of_occupied_from_db(user, container_type)
    context = {
        'user_id': user_id,
        'triples': list_of_triples,
    }
    context.update(base_context(request))
    return render(request, 'accounts/parts/container_table.html', context)

# Ниже неотлаженный код
#########################


def student_make_request(request, user_id, container_type, request_type, container_id):
    user = request.user
    student_request = Request()
    student_request.student = user
    student_request.container = Container.objects.get(id=container_id)
    student_request.status = 0
    student_request.request_type = request_type
    student_request.save()
    return student_form(request, user_id, container_type)

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
    return render(request, 'accounts/parts/requests_table_with_buttons.html', context)


def professor_request_change_status(request, user_id1, request_type, user_id2, status):
    user = request.user
    student_request = Request.objects.get(student=User.objects.get(user_id=user_id2), request_type=request_type, container=Container.objects.get(container_director=user))
    student_request.status = status
    student_request.save()

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
    return render(request, 'accounts/parts/requests_table_with_buttons.html', context)


def sc_dir_request_change_status(request, user_id1, user_id2, request_status):
    user = request.user
    student_request = Request.objects.get(student=User.objects.get(user_id=user_id2), request_type='SCIENCE_HEAD', container=Container.objects.get(container_director=user))
    student_request.status = request_status
    student_request.save()

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
    return render(request, 'accounts/parts/requests_table_without_buttons.html', context)



















