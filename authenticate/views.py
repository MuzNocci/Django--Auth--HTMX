import re
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout



@csrf_protect
def login(request):


    error = {}

    if request.method == 'POST':
        
        email = request.POST.get('inputEmail')
        password = request.POST.get('inputPassword')
        remember = request.POST.get('inputRemember')
        
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            auth_login(request, user)
            if not remember:
                request.session.set_expiry(0) 
            return redirect('show_films')
        else:
            error['login'] = 'Invalid email or password.'
        

    context = {
        'data' : request.POST,
        'error' : error,
    }
    return render(request, 'login.html', context)



@csrf_protect
def register(request):


    error = {}

    if request.method == 'POST':

        name = request.POST.get('inputName')
        split_name = name.split(' ')
        first_name = split_name[0]
        last_name = ''

        if len(split_name) > 1:
            for i in range(len(split_name)):
                if i != 0:
                    last_name += split_name[i]+' '
            last_name = last_name[:-1]
        else:
            last_name = ''

        name = name.replace(' ', '')
        if name:
            for i in range(len(name)):
                if not name[i].isalpha():
                    error['name'] = 'The name can only contain letters.'
            if len(name) <= 2 and error['name'] == '':
                error['name'] = 'The name must have more characters.'
        else:
            error['name'] = 'The name cannot be empty.'


        email = request.POST.get('inputEmail')
        if email:
            if not re.search(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+', email) != None:
                error['email'] = 'The email is invalid.'
            else:
                user = User.objects.filter(username__exact=email)
                if user:
                    error['email'] = 'The email already registered.'
        else:
            error['email'] = 'The email cannot be empty.'


        password = request.POST.get('inputPassword')
        if password:
            if password.replace(' ','') != request.POST.get('inputPassword'):
                error['pass'] = 'The password cannot contain white space.'
            else:
                if len(password.replace(' ','')) < 8:
                    error['pass'] = 'The password must contain 8 characters or more.'
        else:
            error['pass'] = 'The email cannot be empty.'


        repassword = request.POST.get('inputRepeatPassword')
        if repassword:
            if not password == repassword:
                    error['confirm_pass'] = 'The password and confirmation are not the same.'
        else:
            error['confirm_pass'] = 'Repeat the password.'
        

        if len(error) == 0:
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=email, password=password)
            user.save()
            return redirect('login')


    context = {
        'data' : request.POST,
        'error' : error,
    }
    return render(request, 'register.html', context)



@login_required
def logout(request):
    

    auth_logout(request)
    

    return redirect('login')