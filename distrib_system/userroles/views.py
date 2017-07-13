from django.shortcuts import render, render_to_response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .utils import get_entity_from_db, initialize_user
from .models import Student, Cooperator, Professor, ScientificDirector

# Create your views here.


def register(request):
    if request.method == "POST":
        user = User(username=request.POST['username'])
        user.set_password(request.POST['password'])
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()
        positions = request.POST.getlist('position')
        initialize_user(user, positions)
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            messages.add_message(request, messages.INFO, 'Incorrect')
            return HttpResponseRedirect('/accounts/my_profile/' + str(user.id))
    return render(request, 'register.html')


def new_login(request):
    if request.POST:
        username = request.POST.get('login')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/accounts/my_profile/' + str(user.id))
            else:
                raise Http404
        else:
            messages.add_message(request, messages.INFO, 'Неправильный логин или пароль')
            mess = messages.get_messages(request)
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def new_logout(request):
    
    logout(request)
    return HttpResponseRedirect('/accounts/login/')
                

@login_required(login_url='/accounts/login')
def my_profile(request, user_id):

    """Профиль текущего пользователя"""
    user = request.user
    user_entities = get_entity_from_db(user)
    is_student = True if user_entities["std"] is not None else False
    is_professor = True if user_entities["prof"] is not None else False
    is_cooperator = True if user_entities["coop"] is not None else False
    is_sci_director = True if user_entities["scdir"] is not None else False
    context = {
        "user_id": user.id,
        "user_surname": user.last_name,
        "user_name": user.first_name,
        "user_email": user.email,
        "is_student": is_student,
        "is_professor": is_professor,
        "is_cooperator": is_cooperator,
        "is_sci_director": is_sci_director
    }
    
    return render(request, "accounts/my_profile.html", context)


@login_required(login_url='/accounts/login')
def edit_profile(request, user_id):    
    pass


@login_required(login_url='/accounts/login')
def edit_password(request, user_id):    
    pass
