from django.shortcuts import render
from conseil.models import Post
# Create your views here.

def index(request):
    posts = Post.published.all()[:3]
    return render(request, 'main/index.html', {'posts':posts})
