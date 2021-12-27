from django.db import models
from datetime import datetime

# Create your models here.
class Position(models.Model):
    rank = models.PositiveSmallIntegerField(null= True, blank= True, default = 1)
    name = models.CharField(max_length=50)
  

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)
  

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=50)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254)
    linkeden = models.URLField(max_length=200,null=True,blank=True)
    pic = models.ImageField(upload_to='team', height_field=None, width_field=None, max_length=None,default="", null=True, blank="True")
    is_alumnus = models.BooleanField(default = True)
    year = models.PositiveSmallIntegerField(default = datetime.now().year)

    def __str__(self):
        return self.name