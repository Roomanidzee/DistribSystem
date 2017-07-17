from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .utils import *

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
            if user.is_active:
                login(request, user)
                messages.add_message(request, messages.INFO, 'Incorrect')
                return HttpResponseRedirect('/accounts/my_profile/' + str(user.id))
            else:
                messages.add_message(request, messages.INFO, 'Your account is not active')
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
            messages.get_messages(request)
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def new_logout(request):
    
    logout(request)
    return HttpResponseRedirect('/accounts/login/')
                

@login_required(login_url='/accounts/login')
def base_context(request):
    user = request.user
    is_student = get_entity_from_db(user,'Student')
    is_cooperator = get_entity_from_db(user,'Cooperator')
    is_professor = get_entity_from_db(user,'Professor')
    is_sci_director = get_entity_from_db(user,'ScientificDirector')
    context = {
        "user_id": user.id,
        "user_surname": user.last_name,
        "user_name": user.first_name,
        "user_email": user.email,
        "user_username": user.username,
        "is_student": is_student,
        "is_professor": is_professor,
        "is_cooperator": is_cooperator,
        "is_sci_director": is_sci_director
    }
    return context


@login_required(login_url='/accounts/login')
def my_profile(request, user_id):
    return render(request, "accounts/parts/my_data.html", base_context(request))


@login_required(login_url='/accounts/login')
def edit_profile(request, user_id):
    user = request.user
    if request.POST["user_new_name"] is not "":
        user.first_name = request.POST["user_new_name"]
    if request.POST["user_new_surname"] is not "":
        user.last_name = request.POST["user_new_surname"]
    if request.POST["user_new_username"] is not "":
        user.username = request.POST["user_new_username"]
    if request.POST["user_new_email"] is not "":
        user.email = request.POST["user_new_email"]
    user.save()
    return my_profile(request, user_id)


@login_required(login_url='/accounts/login')
def edit_password(request, user_id):    
    user = request.user