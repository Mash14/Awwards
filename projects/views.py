from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Profile,Project

# Create your views here.

def home_page(request):
    profiles = Profile.objects.all()
    projects = Project.objects.all()

    return render(request, 'index.html', {'profiles':profiles,'projects':projects})