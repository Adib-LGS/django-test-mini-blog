from django.shortcuts import render

#from .mocks import Post
from .models import Post
# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'posts' : posts})

def show(request, id):
    post = Post.objects.get(pk=id)
    return render(request, 'blog/show.html', {'post' : post})