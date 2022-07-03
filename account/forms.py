import email
from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models


class UserForm(UserCreationForm):
    class Meta:
        model=models.User
        fields=['username','email']

class CreateProfileForm(forms.ModelForm):
    class Meta:
        model=models.CreateProfile
        exclude = ('user',)

class ChangeForm(forms.ModelForm):
    class Meta:
        model=models.User
        fields=['picture']
        