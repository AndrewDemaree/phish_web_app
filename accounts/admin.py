from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        'email',
        'username',
        'age',
        'is_staff',
        'favorite_phish_song',
        'favorite_fish',
        ]
    fieldsets = UserAdmin.fieldsets + ((None, {'fields': (
        'age',
        'favorite_phish_song',
        'favorite_fish',
        )}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {'fields': (
        'age',
        'favorite_phish_song',
        'favorite_fish',
        )}),)

admin.site.register(CustomUser, CustomUserAdmin)

        
        
