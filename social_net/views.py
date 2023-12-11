"""
Views File
"""
from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from social_net.models import Post, Comment, Like
from django.contrib.auth.models import User
from social_net.forms import CommentForm
from django.http import JsonResponse


class LikePostView(View):
    """
    View for handling post likes.

    Methods:
        - post(request, pk): Handles the HTTP POST request to like/unlike a post.

    Returns:
        A JSON response containing the updated likes count and whether the user liked/unliked the post.
    """

    def post(self, request, pk):
        """
        Handles the HTTP POST request to like/unlike a post.
        """
        post = get_object_or_404(Post, pk=pk)
        user = request.user

        # Check if the user has already liked the post
        if user in post.likes.all():
            post.likes.remove(user)
            is_liked = False
        else:
            post.likes.add(user)
            is_liked = True

        likes_count = post.likes.count()

        return JsonResponse({"likes_count": likes_count, "is_liked": is_liked})


class PostDetailView(DetailView):
    """
    View for displaying a detailed view of a post.

    Methods:
        - get_context_data(**kwargs): Adds additional context data to be used in the template.
        - post(request, *args, **kwargs): Handles the HTTP POST request to add a comment to the post.

    Returns:
        A detailed view of a post.
    """
    model = Post
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        """
        Adds additional context data to be used in the template.
        """
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        """ Handles the HTTP POST request to add a comment to the post."""
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = self.request.user
            comment.post = self.object
            comment.save()
            return redirect('LifeLoader-post_detail', self.object.id)
        return self.render_to_response(self.get_context_data())


class PostCreateView(LoginRequiredMixin, CreateView):
    """
    View for creating new posts.

    Methods:
        - form_valid(form): Sets the author of the post to the current logged-in user.

    Returns:
        A view for creating new posts.
    """
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        """ Sets the author of the post to the current logged-in user. """
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    View for updating posts.

    Methods:
        - form_valid(form): Sets the author of the post to the current logged-in user.
        - test_func(): Checks if the current user is the author of the post.

    Returns:
        A view for updating posts.
    """
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        """ Sets the author of the post to the current logged-in user. """
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        """ Checks if the current user is the author of the post. """
        post = self.get_object()
        if post.author == self.request.user:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    View for deleting posts.

    Methods:
        - test_func(): Checks if the current user is the author of the post.

    Returns:
        A view for deleting posts.
    """
    model = Post
    context_object_name = 'post'
    success_url = '/'

    def test_func(self):
        """ Checks if the current user is the author of the post. """
        post = self.get_object()
        if post.author == self.request.user:
            return True
        return False


def post_list(request):
    """
    View for rendering the post list page.

    Returns:
        A rendered post list page.
    """
    return render(request, 'social_net/post_list.html')


def user_posts(request, username):
    """
    View for rendering the user-specific posts page.

    Parameters:
        - request: The HTTP request object.
        - username: The username of the target user.

    Returns:
        A rendered user-specific posts page.
    """
    return render(request, 'social_net/user_posts.html', {"username": username})


def about(request):
    """
    View for rendering the about page.

    Returns:
        A rendered about page.
    """
    return render(request, 'social_net/about.html', {"title": "About"})
