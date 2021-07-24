from django.db import models
from PIL import Image
from django.urls import reverse

# Create your models here.

class Event(models.Model):
    title  = models.CharField(max_length=50)
    # Specify location for 'default' and 'upload_to'
    # bg_image_id = models.ImageField(default='default.jpg',null=True,upload_to='media/events/')
    bg_image_id = models.CharField(blank=True,max_length=50)
    yt_link = models.URLField(blank=True,null=True,max_length=300)
    content = models.TextField()

    def __str__(self):
        return self.title
    
    """ def get_absolute_url(self):
        return reverse('events_detail', kwargs={"pk": self.pk}) """
