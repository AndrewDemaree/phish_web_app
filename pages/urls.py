from django.urls import path

from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('random/', RandomPageView.as_view(), name='random'),
    path('success/', SuccessPageView.as_view(), name='success'),
    ]
