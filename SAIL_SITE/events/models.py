from django.db import models

from django.urls import reverse

# Create your models here.

class Event(models.Model):
    title  = models.CharField(max_length=50)
    # Specify location for 'default' and 'upload_to'
    bg_image = models.ImageField(default='',upload_to='',Null=True)
    yt_link = models.URLField(default="",max_length=300,Null=True)
    content = models.TextField()

    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.bg_image.path)

        #   Dimensions are hardcoded, relative method required
        if img.height > 450 or img.width > 350:
            output_size = (450, 350)
            img.thumbnail(output_size)
            img.save(self.bg_image.path)
