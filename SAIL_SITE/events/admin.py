from django.contrib import admin
from .models import Event,Category


# Register your models here.
admin.site.register(Category)
admin.site.register(Event)

