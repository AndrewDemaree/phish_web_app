from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *
  
urlpatterns = [
<<<<<<< HEAD
    path('image_upload', ImageDetailView.as_view(), name = 'image_upload'),
    path('image', ImageSubmitView.as_view(), name = 'chosen_image'),
]
  
=======
    path('image_upload', takeimage, name = 'image_upload'),
    path('image', showimage, name = 'chosen_image'),
    ]

>>>>>>> ee1bfd8fa86c4311ce7f0076745979f4355e77bc
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)

