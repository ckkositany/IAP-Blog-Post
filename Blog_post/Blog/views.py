from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from django.views.generic import (ListView,
                                   DetailView,
                                     CreateView,
                                     UpdateView,
                                     )
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

#Handles the createView
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    #instantiate the current logged user before postting new blog
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
   

   #Handles the updateView
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    #instantiate the current logged user before updating the current blog
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

    # test if user is authorized to update the post
    def test_func(self):
        post = self.get_object()

        if self.request.user == post.author:
            return True
        return False
   

def about(request):
    return render(request, 'Blog/About.html')