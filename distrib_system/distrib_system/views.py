from django.http import HttpResponseRedirect


def autoredirect(request):
    return HttpResponseRedirect('/accounts/login/')

    username = request.POST.get('login')
    password = request.POST.get('password')
