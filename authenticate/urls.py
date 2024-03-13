from django.urls import path
from authenticate import views, vhtmx



urlpatterns = [

    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('', views.logout, name='logout'),

]

htmx = [

    path('', vhtmx.clean_name, name='clean_name'),
    path('', vhtmx.clean_email, name='clean_email'),
    path('', vhtmx.clean_pass, name='clean_pass'),
    path('', vhtmx.confirm_pass, name='confirm_pass'),

]

urlpatterns += htmx