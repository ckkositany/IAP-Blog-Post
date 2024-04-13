from django.urls import path
from .views import (PostListView, 
                    PostDetailView,
                      PostCreateView,
                      PostUpdateView,
                      PostDeleteView,
                      UserPostListView,
                      )
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='Blog-home'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'), # handles specific blog as per its id
    path('post/new/', PostCreateView.as_view(), name='post-create'), # handles new created blog
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'), # handles specific blog as per its id
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'), # deletes specific blog as per its id
    path('about/', views.about, name='Blog-about'),
]