from django.shortcuts import render, render_to_response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from .forms import UserForm
from .utils import get_entity_from_db

# Create your views here.


def register(request):
    user_form = UserForm(request.POST or None)
        
    if user_form.is_valid():
        
        user = user_form.save(commit=False)
        user_data = user_form.cleaned_data
        user.username = user_data['username']
        user.last_name = user_data['last_name']
        user.first_name = user_data['first_name']
        user.email = user_data['email']
        user.set_password(user_data['password'])
        user.save()
        user = authenticate(username=user_data['username'], password=user_data['password'])
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/my_profile/' + str(user.id))
    
    context = {
        
        "form": user_form,
        
    }
        
    return render(request, 'register.html', context)


@login_required
def my_profile(request, user_id):
    
    """Профиль текущего пользователя"""
    user = request.user
    
    entity = get_entity_from_db(user)
    
    context = {
        
        "user": entity,
        "user_id": entity.id,
        "user_surname": entity.surname,
        "user_name": entity.name,
        "user_email": entity.email,
        
    }
    
    return render_to_response("accounts/my_profile.html", context, context_instance=RequestContext(request))

@login_required()
def edit_profile(request, user_id):    
    pass
    
@login_required()
def edit_password(request, user_id):    
    pass    