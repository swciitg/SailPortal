from django.db import models
from PIL import Image
from django.urls import reverse

# Create your models here.

class Event(models.Model):
    title  = models.CharField(max_length=50)
    # Specify location for 'default' and 'upload_to'
    # bg_image_id = models.ImageField(default='default.jpg',null=True,upload_to='media/events/')
    bg_image_id = models.CharField(null=True,max_length=50)
    yt_link = models.URLField(null=True,max_length=300)
    content = models.TextField()

    """ def save(self,*args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.bg_image_id.path)

        #   Dimensions are hardcoded, relative method required
            if img.height > 450 or img.width > 350:
            output_size = (450, 350)
            img.thumbnail(output_size)
            img.save(self.bg_image_id.path)
        """
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('events-detail', kwargs={"pk": self.pk})
