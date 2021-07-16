from django.db import models
from django.utils import timezone
from django.urls import reverse

# Not necessary though
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=70)
    author = models.CharField(max_length=40)
    # Better to keep it as CharField() as only admin is gonna edit this
    # author = models.ForeignKey(User,on_delete=models.CASCADE)
    date_posted = models.DateField(default=timezone.now)
    content = models.TextField()
    blog_link = models.URLField()
    bg_image = models.ImageField(default='blog/dafault-blog.png')


    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse("blog-detail", kwargs={"pk": self.pk})
    
