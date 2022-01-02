from django.urls import path, reverse_lazy
from . import views

app_name='services'
urlpatterns = [

    path('', views.services, name="services"),    
]