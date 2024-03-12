import re
from django.shortcuts import render
from django.contrib.auth.models import User



def login(request):


    context = {}
    return render(request, 'login.html', context)



def register(request):


    error = {}

    if request.method == 'POST':


        name = request.POST.get('inputName', '')
        if name:
            if len(name) > 2:
                for i in range(len(name)):
                    if not name[i].isalpha():
                        error['name'] = 'The name can only contain letters.'
            else:
                error['name'] = 'The name must have more characters.'
        else:
            error['name'] = 'The name cannot be empty.'


        email = request.POST.get('inputEmail', '')
        if email:
            if not re.search(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+', email) != None:
                error['email'] = 'The email is invalid.'
        else:
            error['email'] = 'The email cannot be empty.'


        password = request.POST.get('inputPassword', '')


        repassword = request.POST.get('inputRepeatPassword', '')

        
        if len(error) == 0:
            pass
            # user = User(username=email, email=email,)
            # user.save()


    context = {
        'data' : request.POST,
        'error' : error,
    }
    return render(request, 'register.html', context)