from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Profile,Project
from .forms import ProjectForm

# Create your views here.

def home_page(request):
    profiles = Profile.objects.all()
    projects = Project.objects.all()

    return render(request, 'index.html', {'profiles':profiles,'projects':projects})

@login_required(login_url='/accounts/login')
def post_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit = False)
            project.owner = current_user
            project.save()
            return redirect('homePage')
    
    else:
        form = ProjectForm()
    title = 'Upload Project'
    return render(request, 'post_project.html',{'form':form,'title':title})

def search(request):
    if 'title' in request.GET and request.GET['title']:
        search_term = request.GET.get('title')
        searched_projects = Project.search_project(search_term)
        message = f'{search_term}'

        return render(request, 'search.html', {'message':message, 'projects':searched_projects}) 

    else:
        message = "You haven't searched for any project, try again"
    
    return render(request, 'search.html', {'message': message})

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    projects = Project.objects.filter(owner=current_user).all()
    userProfile = Profile.objects.filter(owner = current_user).first()
    return render(request, 'profile.html', {"projects": projects,'userProfile':userProfile})