from django.urls import path
from users.api.v1.views import ProfileListCreateView, ProfileDetailView

urlpatterns = [
    path('users/', ProfileListCreateView.as_view(),
         name='profile-list-create'),
    path('users/<int:user_id>/',
         ProfileDetailView.as_view(), name='profile-detail'),
]
