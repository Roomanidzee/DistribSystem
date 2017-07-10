from django.shortcuts import render
from django.utils.translation import ugettext as _
from .forms import RegistrationForm
from .models import *

# Create your views here.

def register(request):

    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        user.username = form.cleaned_data['username']
        user.set_password(form.cleaned_data['password'])
        user.first_name = form.cleaned_data['first_name']
        user.last_name = form.cleaned_data['last_name']
        user.save()
    context = {
        "form": form,
    }
    return render(request, 'register.html', context)
        