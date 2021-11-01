from django.urls import path, reverse_lazy
from . import views
from .views import BlogListView,BlogDetailView
# from .views import BlogDetailView

app_name='blog'
urlpatterns = [
    path('', BlogListView.as_view(),name='blog-home'),
    path('<int:pk>/', BlogDetailView.as_view(), name = 'blog_detail'),

]