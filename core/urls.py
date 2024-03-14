from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [

    path('admin/', admin.site.urls),
    path('', lambda request: redirect('show_films', permanent=False)),
    path('auth/', include('authenticate.urls')),
    path('films/', include('films.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)