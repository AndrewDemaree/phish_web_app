from django.contrib.auth.models import AbstractUser
from django.db import models


phish_choices = (
    ('1', 'Lushington'),
    ('2', 'You Enjoy Myself'),
    ('3', 'Divided Sky'),
    ('4', 'Tweezer'),
    ('5', 'Reba'),
    ('6', 'Harry Hood'),
    ('7', 'Fluffhead'),
    ('8', 'The Lizards'),
    ('9', 'Run Like an Antelope'),
    ('10', 'Farmhouse'),
    )

fish_choices = (
    ('1', 'Coelacanth'),
    ('2', 'Trout'),
    ('3', 'Pike'),
    ('4', 'Bass'),
    ('5', 'Butterflyfish'),
    ('6', 'Catfish'),
    ('7', 'Clownfish'),
    ('8', 'Lionfish'),
    ('9', 'Tuna'),
    ('10', 'Betta Fish'),
    )

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    favorite_phish_song = models.TextField(null=True, blank=True)
    favorite_fish = models.TextField(null=True, blank=True)
