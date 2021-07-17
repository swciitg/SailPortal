from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView
from django.views.generic import DetailView,CreateView,UpdateView,DeleteView

from .models import Blog

# Create your views here.
def home(request):
    context = {
        'blogs': Blog.objects.all()
    }
    return render(request, 'blog/home.html',context)

class BlogListView(ListView):
    model = Blog
    template_name = "blog/home.html"
    context_object_name = 'blogs'
    ordering = ['-date_posted']

# Not required until external links are used
class BlogDetailView(DetailView):
    model = Blog


# To be worked upon

class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    fields = ['title', 'content']

    # Need to check for admin

    """ def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form) """


class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Blog
    fields = ['title', 'content']

    # Need to check for admin
    """ 
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        Blog = self.get_object()
        if self.request.user == blog.author:
            return True
        return False """


class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Blog
    success_url = '/'

    # Need to check for admin
    """ 
    def test_func(self):
        Blog = self.get_object()
        if self.request.user == Blog.author:
            return True
        return False
    """