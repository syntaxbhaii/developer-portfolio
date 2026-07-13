from django.shortcuts import render
from django.views import View
from .models import Internship
from projects.models import Project # <-- Grabbing Project from your original 'projects' app!

class HomeView(View):
    def get(self, request, *args, **kwargs):
        projects = Project.objects.all()
        internships = Internship.objects.all()
        
        context = {
            'projects': projects,
            'internships': internships,
        }
        
        return render(request, 'portfolio/home.html', context)