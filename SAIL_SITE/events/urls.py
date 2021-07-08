from django.urls import path, reverse_lazy
from . import views
from .views import EventListView,EventDetailView, event

app_name='events'
urlpatterns = [
    path('events/',EventListView.as_view(),name='event-home'),
    path('events/<int:pk>/', EventDetailView.as_view(), name='events-detail'),

    
    

]