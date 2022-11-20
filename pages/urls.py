from django.urls import path

from .views import HomePageView, AboutPageView, RandomPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('random/', RandomPageView.as_view(), name='random'),
    ]
