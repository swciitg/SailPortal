from django.db import models

from .models import Event,Category
from django.shortcuts import render
from django.views.generic import ListView,DetailView

# Create your views here.


def event(request):
    context = {
        
        'categorys': Category.objects.all()
    }
    
    return render(request, 'events/home.html', context=context)


class EventListView(ListView):
    model = Category
    template_name = 'events/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'categorys'
    ordering = ['name']
  

def EventDetailView(request,evnts):
    category_evnts = Event.objects.filter(category=evnts)
    return render(request,'events/events_detail_str.html',{'evnts':evnts,'category_evnts':category_evnts})
   
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
 