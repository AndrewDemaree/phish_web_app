from django.db import models
from django.conf import settings
from django.urls import reverse

class Image(models.Model):
    name= models.CharField(max_length=500)
    imagefile= models.FileField(
        upload_to='images/',
        null=True,
        blank=True,
        verbose_name=""
        )

    def __str__(self):
        return self.name + ": " + str(self.imagefile)
# Create your models here.

class Comment(models.Model):
    comment = models.CharField(max_length=180)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.comment
    def author_grabsie(self):
        return self.author
    def get_absolute_url(self):
        return reverse("comment_detail", kwargs={"pk": self.pk})

