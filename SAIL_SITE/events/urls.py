from django.urls import path, reverse_lazy

app_name='events'
app_name = 'categorys'
urlpatterns = [

    path('',EventListView.as_view(),name='events-home'),
    #path('<int:pk>/', EventDetailView.as_view(), name='events_detail'),
    
    path('<str:evnts>', views.EventDetailView, name='events_detail_str'),

]