from django.urls import path
from .views import (PostListView, 
                    PostDetailView,
                      PostCreateView,
                      PostUpdateView,
                      )
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='Blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'), # handles specific blog as per its id
    path('post/new/', PostCreateView.as_view(), name='post-create'), # handles new created blog
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'), # handles specific blog as per its id
    path('about/', views.about, name='Blog-about'),
]