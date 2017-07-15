from django.contrib.auth.models import User
from django.shortcuts import render

from .models import Request, Container
from .utils import get_practice_with_number_of_occupied_from_db, get_course_with_number_of_occupied_from_db, \
    get_lab_with_number_of_occupied_from_db, get_sci_dir_with_number_of_occupied_from_db

# Create your views here.
'''
    Короче, сюда лезть только готовыми к дикой боли и дебаггингу))
'''
'''
STUDENTS HERE
'''


def student_practice_form(request, user_id):
    user = request.user
    list_of_pairs = get_practice_with_number_of_occupied_from_db(user)
    context = {
        'user_id': user_id,
        'pairs': list_of_pairs,
    }
    return render(request, 'accounts/parts/container_table.html', context)


def student_course_form(request, user_id):
    user = request.user
    list_of_pairs = get_course_with_number_of_occupied_from_db(user)
    context = {
        'user_id': user_id,
        'pairs': list_of_pairs,
    }
    return render(request, 'accounts/parts/container_table.html', context)


def student_lab(request, user_id):
    user = request.user
    list_of_pairs = get_lab_with_number_of_occupied_from_db(user)
    context = {
        'user_id': user_id,
        'pairs': list_of_pairs,
    }
    return render(request, 'accounts/parts/container_table.html', context)


def student_sci_dir(request, user_id):
    user = request.user
    list_of_pairs = get_sci_dir_with_number_of_occupied_from_db(user)
    context = {
        'user_id': user_id,
        'pairs': list_of_pairs,
    }
    return render(request, 'accounts/parts/container_table.html', context)


# Ниже неотлаженный код
#########################


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
    user = request.user
    requests = list(Request.objects.filter(request_type='PRACTICE', container=Container.objects.get(container_director=user)))
    context = {
        "requests": requests,
    }
    context.update(base_context(request))
    return render(request, 'distribution/practice_table.html', context)
    
def professor_choice_course_form(request, user_id):
    user = request.user
    requests = list(Request.objects.filter(request_type='COURSE', container=Container.objects.get(container_director=user)))
    context = {
        "requests": requests,
    }
    context.update(base_context(request))
    return render(request, 'distribution/course_table.html', context)

def professor_lab_form(request, user_id):
    user = request.user
    requests = list(Request.objects.filter(request_type='LAB', container=Container.objects.get(container_director=user)))
    context = {
        "requests": requests,
    }
    context.update(base_context(request))
    return render(request, 'distribution/lab_table.html', context)
    
def professor_practice_accept(request, user_id1, user_id2, status):
    user = request.user
    request = Request.objects.get(student=User.objects.get(user_id=user_id2), request_type='PRACTICE', container=Container.objects.get(container_director=user))
    request.status = 1
    request.save()


def professor_course_accept(request, user_id1, user_id2):
    user = request.user
    request = Request.objects.get(student=User.objects.get(user_id=user_id2), request_type='COURSE', container=Container.objects.get(container_director=user))
    request.status = 1
    request.save()


def professor_lab_accept(request, user_id1, user_id2):
    user = request.user
    request = Request.objects.get(student=User.objects.get(user_id=user_id2), request_type='LAB', container=Container.objects.get(container_director=user))
    request.status = 1
    request.save()


def professor_practice_decline(request, user_id1, user_id2):
    user = request.user
    request = Request.objects.get(student=User.objects.get(user_id=user_id2), request_type='PRACTICE', container=Container.objects.get(container_director=user))
    request.status = 2
    request.save()


def professor_course_decline(request, user_id1, user_id2):
    user = request.user
    request = Request.objects.get(student=User.objects.get(user_id=user_id2), request_type='COURSE', container=Container.objects.get(container_director=user))
    request.status = 2
    request.save()


def professor_lab_decline(request, user_id1, user_id2):
    user = request.user
    request = Request.objects.get(student=User.objects.get(user_id=user_id2), request_type='LAB', container=Container.objects.get(container_director=user))
    request.status = 2
    request.save()

'''
SCIENCE DIR HERE
'''


def sci_dir_form(request, user_id, request_type):
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
    return render(request, 'distribution/practice_table.html', context)

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


def coop_practice_form(request, user_id, request_type):
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
    return render(request, 'distribution/practice_table.html', context)

def coop_course_form(request, user_id):
    user = request.user
    context = {}
    try:
        requests = list(Request.objects.filter(request_type='COURSE', container=Container.objects.get(container_director=user)))
        context = {
            "requests": requests,
        }
    except:
        messages.add_message(request, messages.INFO, 'Список заявок пуст')
    context.update(base_context(request))
    return render(request, 'distribution/course_table.html', context)

def coop_lab_form(request, user_id):
    user = request.user
    context = {}
    try:
        requests = list(Request.objects.filter(request_type='LAB', container=Container.objects.get(container_director=user)))
        context = {
            "requests": requests,
        }
    except:
        messages.add_message(request, messages.INFO, 'Список заявок пуст')
    context.update(base_context(request))
    return render(request, 'distribution/lab_table.html', context)

def coop_sci_dir_form(request, user_id):
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
    return render(request, 'distribution/sci_dir_table.html', context)




















