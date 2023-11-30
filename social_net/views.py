"""
Views File
"""
from django.shortcuts import render
from social_net.models import Post


def home(request):
    data = {
        'posts': Post.objects.all()
    }
    return render(request, 'social_net/home.html', data)


def about(request):
    return render(request, 'social_net/about.html', {"title": "About"})
