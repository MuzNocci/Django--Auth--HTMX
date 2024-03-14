import re
from django.shortcuts import render
from django.contrib.auth.models import User



def clean_name(request):


    error = ''
    name = request.POST.get('inputName').replace(' ','')

    if name:
        for i in range(len(name)):
            if not name[i].isalpha():
                error = 'The name can only contain letters.'
        if len(name) <= 2 and error == '':
            error = 'The name must have more characters.'
    else:
        error = 'The name cannot be empty.'


    context = {
        'error' : error,
    }
    return render(request, 'partials/error.html', context)



def clean_email(request):
    

    error = ''
    email = request.POST.get('inputEmail')

    if email:
        if not re.search(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+', email) != None:
            error = 'The email is invalid.'
        else:
            user = User.objects.filter(username__exact=email)
            if user:
                error = 'The email already registered.'
    else:
        error = 'The email cannot be empty.'


    context = {
        'error' : error,
    }
    return render(request, 'partials/error.html', context)



def clean_pass(request):


    error = ''
    password = request.POST.get('inputPassword')

    if password:
        if password.replace(' ','') != request.POST.get('inputPassword'):
            error = 'The password cannot contain white space.'
        else:
            if len(password.replace(' ','')) < 8:
                error = 'The password must contain 8 characters or more.'
    else:
        error = 'The email cannot be empty.'


    context = {
        'error' : error,
    }
    return render(request, 'partials/error.html', context)



def confirm_pass(request):
    

    error = {}
    password = request.POST.get('inputPassword')
    repassword = request.POST.get('inputRepeatPassword')

    if repassword:
        if not password == repassword:
            error = 'The password and confirmation are not the same.'
    else:
        error = 'Repeat the password.'


    context = {
        'error' : error,
    }
    return render(request, 'partials/error.html', context)