
from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView


urlpatterns = [
    path('', PostListView.as_view(), name = "blog-home"), #empty path is default
    path('user/<str:username>', UserPostListView.as_view(), name = "user-posts"),
    path('post/<int:pk>/', PostDetailView.as_view(), name = "post-detail"), #pk is convention for primary key for detail view
    path('post/new/', PostCreateView.as_view(), name = "post-create"), 
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name = "post-update"), 
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name = "post-delete"),
    path('about/', views.about, name = "blog-about"),
]




