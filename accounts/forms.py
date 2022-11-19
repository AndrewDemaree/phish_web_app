from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser, phish_choices, fish_choices
from django import forms


class CustomUserCreationForm(UserCreationForm):
    age = forms.IntegerField()
    favorite_phish_song = forms.ChoiceField(choices = phish_choices, label = 'Favorite Phish Song')
    favorite_fish = forms.ChoiceField(choices = fish_choices, label = 'Favorite Fish')
    
    class Meta(UserCreationForm):
        model = CustomUser
        fields = (
            'username',
            'email',
            'age',
            'favorite_phish_song',
            'favorite_fish',
            )

class CustomUserChangeForm(UserChangeForm):
    age = forms.IntegerField()
    favorite_phish_song = forms.ChoiceField(choices = phish_choices, label = 'Favorite Phish Song')
    favorite_fish = forms.ChoiceField(choices = fish_choices, label = 'Favorite Fish')

    
    class Meta(UserChangeForm):
        model = CustomUser
        fields = (
            'username',
            'email',
            'age',
            'favorite_phish_song',
            'favorite_fish',
            )
