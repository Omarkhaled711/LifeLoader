
"""
The urls for our api
"""
from django.urls import path
from social_net.api.v1.views import PostListView, UserPostListView

urlpatterns = [
    path('posts/', PostListView.as_view(), name='post-list'),
    path('user_posts/<str:username>/',
         UserPostListView.as_view(), name='user_post_list')
]
