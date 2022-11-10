from django.urls import path
from .views import AuthURL #importing the Authurl class

urlpatterns = [
    path('get-auth-url', AuthURL.as_view()),
]