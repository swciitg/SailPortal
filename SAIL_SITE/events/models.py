from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Event(models.Model):
    title  = models.CharField(max_length=50)
    # Specify location for 'default' and 'upload_to'
    image = models.ImageField(default='',upload_to='')

    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

'''
class Alumni_Talk(models.Model):
    title  = models.CharField(max_length=50)
    image = models.ImageField(default='',upload_to='')

    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Webinar(models.Model):
    title  = models.CharField(max_length=50)
    image = models.ImageField(default='',upload_to='')

    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Graduation_Tea_Party(models.Model):
    title  = models.CharField(max_length=50)
    image = models.ImageField(default='',upload_to='')

    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class International_Students_Day(models.Model):
    title  = models.CharField(max_length=50)
    image = models.ImageField(default='',upload_to='')

    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Finalis_Resonare(models.Model):
    title  = models.CharField(max_length=50)
    image = models.ImageField(default='',upload_to='')

    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Students_Alumni_Meet(models.Model):
    title  = models.CharField(max_length=50)
    image = models.ImageField(default='',upload_to='')

    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
'''