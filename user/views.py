from django.shortcuts import render
from projects.models import Project
from blog.models import Post
from .models import Profile
import datetime

# Create your views here.
def home(request):
    projects = Project.objects.all()
    blogs = Post.objects.all().order_by('-created_on')
    profile = Profile.objects.get(name="Sandesh Nepal")
    
    today = datetime.date.today()
    year = today.year
    context = {
        'projects': projects,
        'blogs': blogs,
        'profile': profile,
        'year': year
        }
    return render(request, 'home.html', context)
