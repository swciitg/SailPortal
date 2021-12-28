from django.db import models

from .models import Event,Category
from django.shortcuts import render
from django.views.generic import ListView,DetailView

# Create your views here.


def event(request):
    context = {
        'events': Event.objects.all()
    }
    
    return render(request, 'events/home.html', context=context)


class EventListView(ListView):
    model = Event
    template_name = 'events/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'events'
    ordering = ['title']
  

""" def EventDetailView(request,evnts):
    event_evnts = Event.objects.filter(event=evnts)
    return render(request,'events/events_detail_str.html',{'evnts':evnts,'event_evnts':event_evnts}) """

class EventDetailView(DetailView):
    model = Event
    context_object_name = 'events'
    template_name = "events/events_detail.html"

"""   
    
class EventDetailView(DetailView):
    model = Category
    #context_object_name = 'categorys'
    template_name = "events/events_detail.html"
     """
"""     def get_context_data(self,**kwargs):
            events = super().get_context_data(**kwargs)
            category = Category.objects.get( category = self.id)    
            events['events'] = Event.objects.all().filter(category=category)
            
            return events
 """
 