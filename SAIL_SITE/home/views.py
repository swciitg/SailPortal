from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from .models import Pic

class PicListView(ListView):
    model = Pic
    template_name = "home/home.html"

    # def get_context_data(self, **kwargs):
    #     context = super(PicListView, self).get_context_data(**kwargs)
    #     context['pic_list'] = Team.objects.all()
    #     context['about_list'] = About.objects.all()
    #     context['sponsor_list'] = OurSponsor.objects.all()
        # return context