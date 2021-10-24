from django.db import models
from PIL import Image
from django.db.models.deletion import CASCADE
from django.urls import reverse
from django.core.validators import FileExtensionValidator



# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30, default='')
    icon = models.ImageField(default='default.jpg',upload_to='events/')
        
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('events/home.html')
    
    
class Event(models.Model):
    category = models.ForeignKey(Category,related_name='events',on_delete=models.CASCADE,default='Uncategorized')
    
    title = models.CharField(max_length=100, blank=True, default='')
    link = models.URLField(blank=True, null=True,max_length=200)
    content = models.TextField(default='')


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('events_detail_str', kwargs={"evnts": self.category})
        
