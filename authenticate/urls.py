from django.urls import path
from authenticate import views, vhtmx



urlpatterns = [

    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

]

htmx = [

    path('clean_name', vhtmx.clean_name, name='clean_name'),
    path('clean_email', vhtmx.clean_email, name='clean_email'),
    path('clean_pass', vhtmx.clean_pass, name='clean_pass'),
    path('confirm_pass', vhtmx.confirm_pass, name='confirm_pass'),

]

urlpatterns += htmx