from django.db import models
import os

def get_image_path(instance, filename):
    return os.path.join('images/', filename)

class Image(models.Model):
    image = models.ImageField(upload_to=get_image_path)
    
    