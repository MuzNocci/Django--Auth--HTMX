from django.contrib import admin
from django.urls import path, include



urlpatterns = [

    path('admin/', admin.site.urls),
    path('auth/', include('authenticate.urls')),
    path('films/', include('films.urls')),

]
