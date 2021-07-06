from django.urls import path, reverse_lazy
from . import views
from .views import EventListView,EventDetailView, event

#   Not yet completed yet
from .views import EventCreateView,EventUpdateView,EventDeleteView

app_name='events'
urlpatterns = [
    path('events/',EventListView.as_view(),name='event-home'),
    path('events/<int:pk>/', EventDetailView.as_view(), name='events-detail'),

    
    #   Used afterwards
    '''
    path('events/new/', EventCreateView.as_view(), name='events-create'),
    path('events/<int:pk>/update/', EventUpdateView.as_view(), name='events-update'),
    path('events/<int:pk>/delete/', EventDeleteView.as_view(), name='events-delete'),
    '''

]