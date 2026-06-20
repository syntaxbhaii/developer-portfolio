from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView
from .models import BlogPost

class PostDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/post_detail.html'
    context_object_name = 'post' # This allows us to use {{ post.title }} in the HTML