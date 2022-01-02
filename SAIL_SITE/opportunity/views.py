from django.shortcuts import render
from .models import Opportunity
from .forms import OppForm
# Create your views here.
from django.views.generic import ListView,DetailView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy,reverse

class OpportunityListView(ListView):
    model = Opportunity
    template_name = "opportunity/home.html"
    ordering = ['-published']
    queryset= Opportunity.objects.all()


class TagView(ListView):
    model = Opportunity
    template_name = "opportunity/home.html"
    
    def get_queryset(self):
        return Opportunity.objects.filter(tags__slug=self.kwargs.get('tag_slug'))

class OpportunityDetail(DetailView):
    model = Opportunity
    template_name='opportunity/detail.html'


class OpportunityCreateView(CreateView,LoginRequiredMixin):
    form_class = OppForm
    template_name = 'opportunity/create.html'
    def get_success_url(self):
        return reverse('opportunity:home')