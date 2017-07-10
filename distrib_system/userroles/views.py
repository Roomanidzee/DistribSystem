from django.shortcuts import render, render_to_response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from .forms import UserForm, UserProfileForm
from .models import UserProfile

# Create your views here.

def register(request):
    
    user = User()
    user_profile = UserProfile()
        
    user_form = UserForm(request.POST, instance = user)
    user_profile_form = UserProfileForm(request.POST, instance = user_profile)
        
    if user_form.is_valid() and user_profile_form.is_valid():
            
        user_data = user_form.cleaned_data
        user.username = user_data['username']
        user.last_name = user_data['last_name']
        user.first_name = user_data['first_name']
        user.email = user_data['email']
        user.set_password(user_data['password'])
        user.save()
            
        user_profile = user.get_profile()
        user_profile_data = user_profile_form.cleaned_data
        user_profile.type = user_profile_data['type']
        user_profile.patronymic = user_profile_data['patronymic']
        user_profile.save()
            
        user = authenticate(username = user_data['username'], password = user_data['pass1'])
        login(request, user)
        return HttpResponse("profile/")
        
    context = {
        "form": user_form,
        "profile_form": user_profile_form,
    }
        
    return render(request, 'register.html', context)
    
@login_required
def my_profile(request):
    
    """Профиль текущего пользователя"""
    user = request.user
    return render_to_response( "accounts/card.html", { "user": user }, context_instance = RequestContext( request ) )    