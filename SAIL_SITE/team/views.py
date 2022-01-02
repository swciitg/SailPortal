from django.shortcuts import render
from .models import Team
# Create your views here.
from django.views.generic import ListView
from django.db.models import Q

def TeamListView(request):
    team =  Team.objects.filter(Q(is_alumnus=False)).order_by("position__rank")
    pastmemberlist =  Team.objects.filter(Q(is_alumnus=True), Q(position__name ="General Secretary")).order_by("-year")
    print(team)
    return render(request, "team/team_list.html", {"team": team, "pastmemberlist": pastmemberlist})