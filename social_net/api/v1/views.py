from rest_framework import generics, permissions
from rest_framework.pagination import PageNumberPagination
from social_net.models import Post, Comment, Like
from social_net.api.v1.serializers import PostSerializer, CommentSerializer, LikeSerializer
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.db.models import Count


class CustomPageNumberPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 300


class PostListView(generics.ListAPIView):
    queryset = Post.objects.annotate(likes_count=Count(
        'likes'), comments_count=Count('comments')).order_by('-date_created')
    serializer_class = PostSerializer
    pagination_class = CustomPageNumberPagination


class UserPostListView(generics.ListAPIView):
    """
    A class for filtering posts based on users
    """
    serializer_class = PostSerializer
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        username = self.kwargs['username']
        user = get_object_or_404(User, username=username)

        # Annotate the queryset with counts of likes and comments
        queryset = Post.objects.filter(author=user).annotate(
            likes_count=Count('likes'),
            comments_count=Count('comments')
        ).order_by('-date_created')

        return queryset


class CommentListView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return Comment.objects.filter(post__id=post_id).select_related('user')

    def perform_create(self, serializer):
        post_id = self.kwargs['post_id']
        serializer.save(user=self.request.user, post_id=post_id)


class LikeListView(generics.ListCreateAPIView):
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return Like.objects.filter(post__id=post_id)

    def perform_create(self, serializer):
        post_id = self.kwargs['post_id']
        serializer.save(user=self.request.user, post_id=post_id)
