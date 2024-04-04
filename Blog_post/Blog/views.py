from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView
from .models import Post

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'Blog/home.html', context)


#creating a list of post
class PostListView(ListView):
    model = Post
    template_name = 'Blog/home.html' #<app>/<model>_<view_type>.html
    context_object_name = 'posts'
    ordering = ['-date_posted'] #change the order to display the latest blogs


#Handles detailview of posts
class PostDetailView(DetailView):
    model = Post
   

def about(request):
    return render(request, 'Blog/About.html')