from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from projects.models import Project

class HomeView(TemplateView):
    template_name = 'portfolio/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Fetch all projects from the database to display on the home page
        context['projects'] = Project.objects.all()
        return context