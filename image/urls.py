from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *
  
urlpatterns = [
    path('submit/image_upload', takeimage, name = 'image_upload'),
    path('submit/image', showimage, name = 'chosen_image'),
    path('chat/', CommentGet.as_view(), name='comment'),
    path('chat/<int:pk>/', CommentDetailView.as_view(), name='comment_detail' ),
    path('chat/<int:pk>/edit', CommentUpdateView.as_view(), name= 'comment_edit'),
    path('chat/new/', CommentCreateView.as_view(), name='comment_new'),
    path('chat/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
    ]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)

