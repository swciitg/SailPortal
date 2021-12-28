from django.db import models
from django.db.models.lookups import EndsWith
from django.utils import timezone
from django.urls import reverse

from ckeditor.fields import RichTextField

# Not necessary though
# from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=70)
    author = models.CharField(max_length=40)
    # Better to keep it as CharField() as only admin is gonna edit this
    # author = models.ForeignKey(User,on_delete=models.CASCADE)
    date_posted = models.DateField(default=timezone.now)

    # content here is the sample content,ie it'll only contain some part ending with ...
    body = RichTextField(blank=True, null=True)
    blog_link = models.URLField(blank=True, null=True)

    thumbnail = models.ImageField(default='default.jpg',upload_to='blogs/',height_field=None, width_field=None, max_length=None, null=True, blank="True")


    def __str__(self):
        return self.title
    
    """ def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"pk": self.pk})
        # return reverse("blog/blog_detail", kwargs={"title": self.title}) """
    
