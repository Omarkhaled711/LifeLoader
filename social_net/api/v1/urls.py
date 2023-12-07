
"""
The urls for our api
"""
from django.urls import path
from social_net.api.v1.views import PostListView, UserPostListView, CommentListView, LikeListView

urlpatterns = [
    path('posts/', PostListView.as_view(), name='post-list'),
    path('user_posts/<str:username>/',
         UserPostListView.as_view(), name='user_post_list'),
    path('posts/<int:post_id>/comments/',
         CommentListView.as_view(), name='comment-list'),
    path('posts/<int:post_id>/likes/', LikeListView.as_view(), name='like-list'),
]
