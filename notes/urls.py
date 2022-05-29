from django.contrib import admin
from django.urls import path
from .views import *
import django.contrib.auth.views as auth_views

urlpatterns = [
    path('', index ,name='index'),
    path('home/', home ,name='home'),
    path('login/',auth_views.LoginView.as_view(template_name='notes/login.html') ,name='login'),
    path('loggedout/', auth_views.LogoutView.as_view(template_name='notes/loggedout.html') ,name='loggedout'),
    path('update/<int:id>/', update ,name='update'),
    path('delete/<int:id>/', delete ,name='delete'),
    path('settings/', settings ,name='settings'),
    path('register/', register ,name='register'),
]
