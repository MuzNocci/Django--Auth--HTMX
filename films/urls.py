from django.urls import path
from films import views



urlpatterns = [

    path('', views.show_films, name='show_films'),
    path('review/<id>', views.details_films, name='details_films'),

]