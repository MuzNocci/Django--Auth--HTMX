import re
from django.shortcuts import render



def clean_name(request):


    error = ''
    name = str(request.POST.get('inputName')).replace(' ','')

    if name:
        if len(name) > 2:
            for i in range(len(name)):
                if not name[i].isalpha():
                    error = 'The name can only contain letters.'
        else:
            error = 'The name must have more characters.'
    else:
        error = 'The name cannot be empty.'


    context = {
        'error' : error,
    }
    return render(request, 'partials/error.html', context)



def clean_email(request):
    

    error = ''
    email = str(request.POST.get('inputEmail'))

    if email:
        if not re.search(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+', email) != None:
            error = 'The email is invalid.'
    else:
        error = 'The email cannot be empty.'


    context = {
        'error' : error,
    }
    return render(request, 'partials/error.html', context)