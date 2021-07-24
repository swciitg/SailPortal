from django.urls import path, reverse_lazy
from . import views
from .views import EventListView,EventDetailView, event

app_name='events'
urlpatterns = [
    path('',EventListView.as_view(),name='events-home'),
    path('<int:pk>/', EventDetailView.as_view(), name='events_detail'),

    
    

]