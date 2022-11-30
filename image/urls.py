from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *
  
urlpatterns = [
    path('image_upload', takeimage, name = 'image_upload'),
    path('image', showimage, name = 'chosen_image'),
    ]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)

