
from django import forms
from .models import Comment
from .models import Image

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("comment", "author")


class ImageForm(forms.ModelForm):
    class Meta:
        model= Image
        fields= ["name", "imagefile"]
