from django.shortcuts import render
from .models import Blog, BlogAuthor, BlogComment
from django.contrib.auth.models import User
from django.views import generic


# Create your views here.
# TODO:: Change to class list view for all the blogs
class BlogListView(generic.ListView):
    """
    Generic class-based view for a list of all blogs.
    """
    model = Blog
    template_name = 'blog/index.html'
