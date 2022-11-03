from django.urls import path
from .views import SignUpView

urlpatterns = [
    path('sighnup/', SignUpView.as_view(), name='signup'),
    ]
