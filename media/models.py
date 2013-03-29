from django.db import models
from django.contrib.auth.models import User
import os



def get_image_path(instance, filename):
    return os.path.join('images/', filename)

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    activation_key = models.CharField(max_length=40)  

class Image(models.Model):
    image = models.ImageField(upload_to=get_image_path)
    user_profile = models.ForeignKey(UserProfile)
    
