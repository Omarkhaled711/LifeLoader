"""
Views File
"""
from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from social_net.models import Post
from django.contrib.auth.models import User


class PostListView(ListView):
    """ A class for listing posts """
    model = Post
    context_object_name = 'posts'
    ordering = ['-date_created']
    paginate_by = 5


class UserPostListView(ListView):
    """ A class for listing posts of a specific user """
    model = Post
    template_name = 'social_net/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        """
        Get the posts by specific user
        """
        user = get_object_or_404(User, username=self.kwargs['username'])
        return Post.objects.filter(author=user).order_by('-date_created')


class PostDetailView(DetailView):
    """ A class for viewing a certain post """
    model = Post
    context_object_name = 'post'


class PostCreateView(LoginRequiredMixin, CreateView):
    """ A class for creating new posts """
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        """ linking the post being created to a specific user """
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """ A class for updating posts """
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        """ linking the post being created to a specific user """
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        """ 
        Allowing editing only if the current user is
        the author of the post
        """
        post = self.get_object()
        if post.author == self.request.user:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """ A class for viewing a certain post """
    model = Post
    context_object_name = 'post'
    success_url = '/'

    def test_func(self):
        """ 
        Allowing editing only if the current user is
        the author of the post
        """
        post = self.get_object()
        if post.author == self.request.user:
            return True
        return False


def about(request):
    return render(request, 'social_net/about.html', {"title": "About"})
