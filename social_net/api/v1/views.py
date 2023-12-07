from rest_framework import generics, permissions
from rest_framework.pagination import PageNumberPagination
from social_net.models import Post
from social_net.api.v1.serializers import PostSerializer
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User


class CustomPageNumberPagination(PageNumberPagination):
    """
    Handling pagination settings
    """
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 300


class PostListView(generics.ListAPIView):
    """ A class for listing posts """
    queryset = Post.objects.all().order_by('-date_created')
    serializer_class = PostSerializer
    pagination_class = CustomPageNumberPagination


class UserPostListView(generics.ListAPIView):
    """
    A class for filtering posts based on users
    """
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        username = self.kwargs['username']
        user = get_object_or_404(User, username=username)
        return Post.objects.filter(author=user).order_by('-date_created')
