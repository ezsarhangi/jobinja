from email.policy import default
from django.forms import Widget
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager


class User(AbstractUser):
    picture = models.ImageField(
        upload_to='profile_picture',
        default='profile_picture/default.jpg')
    bio = models.TextField(null=True, blank=True)
    github_username = models.CharField(max_length=200, null=True, blank=True)
    role = models.CharField(max_length=200, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    objects = CustomUserManager()

    
    def get_absolute_url(self):
        return reverse("profile", kwargs={"username": self.username})      


class CreateProfile(models.Model):
    exp=models.TextField()
    age=models.CharField(max_length=2)
    mobile=models.CharField(max_length=11)
    address=models.TextField()
    city=models.CharField(max_length=11,default='tehran')
    country=models.CharField(max_length=11,default='Iran')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill = models.CharField(max_length=100,default='tehran')

    def __str__(self):
        return f'{self.user.username} Profile'

    
