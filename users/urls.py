from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from users import views

urlpatterns = [
    path('register/', views.register, name="LifeLoader-register"),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'),
         name='LifeLoader-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'),
         name='LifeLoader-logout'),
    path('profile/', views.profile, name="LifeLoader-profile"),
    path('profile/<str:username>/', views.view_profile,
         name="LifeLoader-view_profile"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
