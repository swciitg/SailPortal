from django.shortcuts import render
from .models import upload

# Create your views here.

def initiative(request):
    pics=upload.objects.all()
    return render(request, 'initiatives.html', {"pics":pics})  


