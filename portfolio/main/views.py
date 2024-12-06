from django.shortcuts import render
from .models import Project, Tag

def home(request):
    projects = Project.objects.all()
    tags = Tag.objects.all()
    return render(request, "home.html", {"projects": projects, "tags": tags})

def contact(request):
    return render(request, "contact.html")

def project(request, id):
    return render(request, "project.html")


