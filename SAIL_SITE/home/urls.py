from django.urls import path, reverse_lazy
from . import views


app_name='home'
urlpatterns = [
    path('', views.PicListView.as_view(), name = 'home'),

]