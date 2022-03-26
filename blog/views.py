from django.http import HttpResponse
from django.shortcuts import render
from .models import BlogPost

# Create your views here.


def index(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog/index.html', {'posts':posts})


def blogpost(request, id):
    post = BlogPost.objects.filter(post_id = id)[0]
    return render(request, 'blog/blogpost.html', {'post':post})
