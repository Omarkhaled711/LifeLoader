from django.urls import path
from django.contrib.auth import views as auth_views
from users import views

urlpatterns = [
    path('register/', views.register, name="LifeLoader-register"),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'),
         name='LifeLoader-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'),
         name='LifeLoader-logout')
]
