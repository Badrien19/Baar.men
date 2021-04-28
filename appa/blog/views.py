from django.shortcuts import render
from .models import Post
# Create your views here.

posts = [
    {
        'author': 'Appa',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 26, 2021'
    },
    {
        'author': 'Badrien',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 26, 2021'
    }
]

def home(request):
	context = {
        'posts': Post.objects.all()
    }
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html')