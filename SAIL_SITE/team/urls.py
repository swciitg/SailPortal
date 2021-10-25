from django.urls import path, reverse_lazy
from . import views
from . models import Team

app_name='team'
urlpatterns = [
    path('', views.TeamListView, name='SailTeam'),
    path('past_execs', views.PastExecutives, name="PastExecutives"),
]