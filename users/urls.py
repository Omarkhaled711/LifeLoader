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
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='users/password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
         template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
         template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(
         template_name='users/password_reset_complete.html'), name='password_reset_complete'),
    path('search/', views.user_search, name='LifeLoader-user_search')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
