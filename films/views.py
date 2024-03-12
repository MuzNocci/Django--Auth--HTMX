from django.shortcuts import render



def show_films(request):

    context = {}
    return render(request, 'show_films.html', context)