from django.db import models
import os

def get_image_path(instance, filename):
    return os.path.join('images/', filename)

class Image(models.Model):
    image = models.ImageField(upload_to=get_image_path)
    
    def delete(self, *args, **kwargs):
        # You have to prepare what you need before delete the model
        storage, path = self.image.storage, self.image.path
        # Delete the model before the file
        super(Image, self).delete(*args, **kwargs)
        # Delete the file after the model
        storage.delete(path)
    
    