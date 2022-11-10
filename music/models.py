from operator import mod
from pyexpat import model
from re import T
from statistics import mode
from django.db import models
from django.urls import reverse
# Create your models here.

class Song(models.Model):
    name = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    length = models.CharField(max_length=50)
    song_id = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("song_detail", kwargs={"pk":self.pk})

class SpotifyToken(models.Model):
    user = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField()
    refresh_token = models.CharField(max_length=150)
    access_token = models.CharField(max_length=150)
    expires_in = models.DateTimeField()
    token_type = models.CharField(max_length=50)