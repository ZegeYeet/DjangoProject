
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name = "blog-home"), #empty path means it is the default/home
    path('about/', views.about, name = "blog-about"),
]




