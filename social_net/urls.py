from django.urls import path, include
from social_net import views

urlpatterns = [
    path('', views.PostListView.as_view(), name="LifeLoader-home"),
    path('posts/<str:username>/', views.UserPostListView.as_view(),
         name="LifeLoader-user_posts"),
    path('post/<int:pk>/', views.PostDetailView.as_view(),
         name="LifeLoader-post_detail"),
    path('post/new/', views.PostCreateView.as_view(),
         name="LifeLoader-post_create"),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(),
         name="LifeLoader-post_update"),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(),
         name="LifeLoader-post_delete"),
    path('about/', views.about, name="LifeLoader-about"),
    path('api/v1/', include('social_net.api.v1.urls')),
    path('like_post/<int:pk>/', views.LikePostView.as_view(), name='like_post')
]
