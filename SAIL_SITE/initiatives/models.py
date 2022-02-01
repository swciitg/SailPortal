from django.db import models
from ckeditor.fields import RichTextField

class upload(models.Model):
    title=models.CharField(max_length=50)
    image=models.ImageField(upload_to="img/%y")
    desc=RichTextField(blank=True,null=True)
    url=models.URLField(blank=True, max_length=200)
    urlTitle=models.CharField(max_length=20)

    def __str__(self):
        return self.title




        