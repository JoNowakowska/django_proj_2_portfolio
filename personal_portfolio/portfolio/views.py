from django.shortcuts import render
from .models import Project

import datetime


def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {"date": datetime.date.today(), "projects": projects})
