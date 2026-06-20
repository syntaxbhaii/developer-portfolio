from django.shortcuts import render

from django.views.generic import TemplateView
from projects.models import Project
from blog.models import BlogPost # Import the new model

class HomeView(TemplateView):
    template_name = 'portfolio/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.all()
        # Fetch only the 3 most recent blog posts for the home page
        context['blogs'] = BlogPost.objects.all()[:3] 
        return context