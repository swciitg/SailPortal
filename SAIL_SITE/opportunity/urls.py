from django.urls import path, reverse_lazy
from . import views

app_name='opportunity'
urlpatterns = [
    path('', views.OpportunityListView.as_view(), name="home"),
    path('post', views.OpportunityCreateView.as_view(), name="Post"),
    path('<int:pk>', views.OpportunityDetail.as_view(), name="detail"),
    path('tags/<slug:tag_slug>', views.TagView.as_view(), name="post_by_tag"),
]