from django.urls import path
from social_net import views

urlpatterns = [
    path('', views.home, name="LifeLoader-home"),
    path('about/', views.about, name="LifeLoader-about")
]
