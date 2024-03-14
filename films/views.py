from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from films.models import FilmReview



def show_films(request):

    reviews = FilmReview.objects.all().order_by('-id')

    context = {
        'reviews' : reviews,
    }
    return render(request, 'show_films.html', context)



def details_films(request, id):

    review = FilmReview.objects.filter(id=id)

    context = {
        'review' : review,
    }
    return render(request, 'details_films.html', context)