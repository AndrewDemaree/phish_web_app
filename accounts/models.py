from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    favorite_phish_song = models.PositiveIntegerField(null=True, blank=True)
    favorite_fish = models.PositiveIntegerField(null=True, blank=True)
