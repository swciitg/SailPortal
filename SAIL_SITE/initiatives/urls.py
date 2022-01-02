from django.urls import path, reverse_lazy, include
from . import views

app_name='initiatives'
urlpatterns = [
    path('', views.initiative, name="initiatives"),    
]