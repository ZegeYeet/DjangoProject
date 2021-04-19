from django.shortcuts import render #render returns and http response so don't need to worry about that
#from django.http import HttpResponse
from .models import Post





# Create your views here.
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

