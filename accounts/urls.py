from django.urls import path
from .views import SignUpView, SubmitView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('submit/', SubmitView.as_view(), name='submit'),
    ]
