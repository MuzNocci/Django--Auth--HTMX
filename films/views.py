from django.shortcuts import render
from django.contrib.auth.decorators import login_required



@login_required
def show_films(request):

    context = {}
    return render(request, 'show_films.html', context)