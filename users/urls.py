"""Defines URL patterns for users."""

from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views

app_name = 'users'

urlpatterns = [
    # default auth urls
#    path('', include('django.contrib.auth.urls')),
    # login page
    path('login/',
         auth_views.LoginView.as_view(template_name = 'users/login.html'),
         name = 'login'),
    # logout page
    path('logout/', 
         auth_views.LogoutView.as_view(template_name = 'users/logout.html'), name = 'logout'),
    # users registration
    path('register/', views.register, name = 'register'),
]
