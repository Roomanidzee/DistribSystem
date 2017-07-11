from django.shortcuts import render, render_to_response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from .forms import UserForm

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
            return HttpResponseRedirect('/my_profile/')
    context = {
        "form": user_form,
    }
        
    return render(request, 'register.html', context)


@login_required
def my_profile(request):
    
    """Профиль текущего пользователя"""
    user = request.user
    return render_to_response("accounts/card.html", {"user": user}, context_instance=RequestContext(request))