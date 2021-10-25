from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Profile,Project,Rates
from .forms import ProjectForm,NewProfileForm,RatingsForm
from django.urls import reverse
from django.http.response import HttpResponse, HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import UserSerializer,ProfileSerializer,ProjectSerializer

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
    userProfile = Profile.objects.filter(user = current_user).first()
    return render(request, 'profile.html', {"projects": projects,'userProfile':userProfile})

@login_required(login_url='/accounts/login/')
def update_profile(request):
    current_user = request.user
    userProfile = Profile.objects.filter(user = current_user).first()
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        
        if form.is_valid():
            profile = form.save(commit = False)
            profile.user = current_user
            profile.save()
            return redirect('profile_page')

    else:
        form = NewProfileForm()
        
    title = 'Update Profile'
    return render(request, 'update_profile.html',{'form':form,'title':title,'userProfile':userProfile})

@login_required(login_url='/accounts/login')
def single_project(request, id):
    project = Project.objects.get(id=id)
    rate = Rates.objects.filter(user=request.user, project=project).first()
    ratings = Rates.objects.all()
    rating_status = None
    if rate is None:
        rating_status = False
    else:
        rating_status = True
    current_user = request.user
    if request.method == 'POST':
        form = RatingsForm(request.POST)
        if form.is_valid():
            design = form.cleaned_data['design']
            usability = form.cleaned_data['usability']
            content = form.cleaned_data['content']
            review = Rates()
            review.project = project
            review.user = current_user
            review.design = design
            review.usability = usability
            review.content = content
            review.average = (
                review.design + review.usability + review.content)/3
            review.save()
            return HttpResponseRedirect(reverse('view_project', args=(project.id,)))
    else:
         form = RatingsForm()

    params = {
        'project': project,
        'form': form,
        'rating_status': rating_status,
        'reviews': ratings,
        'ratings': rate

    }
    return render(request, 'view_project.html', params)

class ProfileList(APIView):

    def get(self, request, format=None):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)

class ProjectList(APIView):

    def get(self, request, format = None):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)