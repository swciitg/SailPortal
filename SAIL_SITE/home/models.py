from django.db import models

# Create your models here.
class Pic(models.Model):
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to="home", height_field=None, width_field=None, max_length=None)
    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name
