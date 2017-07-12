from django.shortcuts import render, render_to_response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .forms import UserForm
from . import utils
from .utils import get_entity_from_db

# Create your views here.


def register(request):
    
    if request.method == "POST":
        user = User(username=request.POST['username'])
        user.set_password(request.POST['password'])
        user.first_name=request.POST['first_name']
        user.last_name=request.POST['last_name']
        user.email=request.POST['email']
        user.save()
        positions = request.POST.getlist('position')
        utils.initialize_user(user, positions)
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/accounts/my_profile/'+str(user.id))
    return render(request, 'register.html')


def new_login(request):
    
    username = request.POST['login']
    password = request.POST['password']
    
    user = authenticate(username=username, password=password)
    
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect('/my_profile/'+str(user.id))
        else:
            
            raise Http404
    
    else:            
            raise Http404
        
def new_logout(request):
    
    logout(request)
    return HttpResponseRedirect('/login/')
                


@login_required(login_url = '/accounts/login')
def my_profile(request, user_id):

    """Профиль текущего пользователя"""
    user = request.user

    entity = get_entity_from_db(user)

    context = {

        "user_id": user.id,
        "user_surname": user.surname,
        "user_name": user.name,
        "user_email": user.email,
        
    }
    
    return render_to_response("accounts/my_profile.html", context, context_instance=RequestContext(request))


@login_required(login_url = '/accounts/login')
def edit_profile(request, user_id):    
    pass


@login_required(login_url = '/accounts/login')
def edit_password(request, user_id):    
    pass
