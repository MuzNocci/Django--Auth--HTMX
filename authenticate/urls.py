from django.urls import path
from authenticate import views, vhtmx



urlpatterns = [

    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),

]

htmx = [

    path('clean_name', vhtmx.clean_name, name='clean_name'),
    path('clean_email', vhtmx.clean_email, name='clean_email'),

]

urlpatterns += htmx