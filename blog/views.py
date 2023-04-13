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
    # TODO: Add Pagination by 6 articles


class BlogDetailView(generic.DetailView):
    """
    Generic class-based detail view for a blog.
    """
    model = Blog
    template_name = 'blog/blog-detail.html'


class AutorListView(generic.ListView):
    """
    Generic Class Based View for a list view of all Authors
    """
    model = BlogAuthor
    template_name = 'blog/authors.html'
