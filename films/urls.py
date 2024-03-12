from django.urls import path
from films import views



urlpatterns = [

    path('', views.show_films, name='show_films'),

]