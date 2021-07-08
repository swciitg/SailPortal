from django.db import models
#from SAIL_SITE.events.models import Event
from .models import Event
from django.shortcuts import render
from django.views.generic import ListView,DetailView


from django.views.generic import CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

# Create your views here.

def event(request):
    context = {
        'events': Event.objects.all()
    }
    return render(request, 'events/home.html', context)


class EventListView(ListView):
    model = Event
    template_name = 'events/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'events'
    
class EventDetailView(DetailView):
    model = Event


class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    fields = ['title', 'image']

    '''
    # This func should test if user is admin or not
    def test_func(self):
    '''
        

    


class EventUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Event
    fields = ['title', 'image']

    '''
    # This func should test if user is admin or not
    def test_func(self):
    '''
        


class EventDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Event
    success_url = '/'

    '''
    # This func should test if user is admin or not
    def test_func(self):
    '''
       
