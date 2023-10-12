# blog/views.py
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Post

class BlogListView(ListView):
    model = Post
    template_name = "home.html"

class BlogDetailView(DetailView): # new
    model = Post
    template_name = "post_detail.html"

class BlogCreateView(CreateView): # new
    model = Post
    template_name = "post_new.html"
    fields = ["title", "author", "body"]

class BlogUpdateView(UpdateView): # new
    model = Post
    template_name = "post_edit.html"
    fields = ["title", "body"]