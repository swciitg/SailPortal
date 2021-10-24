from django.db import models
from taggit.managers import TaggableManager
# Create your models here.

class Role(models.Model):
    name = models.CharField(max_length=50)  

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

class Branch(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class Program(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class Year(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Opportunity(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone = models.IntegerField(max_length=11,unique=True)
    company = models.CharField(max_length=80)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE)
    program = models.ForeignKey(Program,on_delete=models.CASCADE)
    year = models.ForeignKey(Year,on_delete=models.CASCADE)
    tags = TaggableManager()
    desc = models.TextField()
    doc = models.FileField(upload_to='docs', max_length=100)
    active = models.BooleanField(default=True)
    published = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name
