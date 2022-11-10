from django.db import models
from django.conf import settings
from django.urls import reverse

class Image(models.Model):
    name= models.CharField(max_length=500)
    videofile= models.FileField(upload_to='images/', null=True, verbose_name="")

    def __str__(self):
        return self.name + ": " + str(self.imagefile)
# Create your models here.

class Comment(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    comment = models.CharField(max_length=140)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse("image_list")

