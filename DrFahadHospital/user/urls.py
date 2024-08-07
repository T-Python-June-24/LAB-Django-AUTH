# user/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='user/registration/login.html'), name='login'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('reservations/', views.user_reservations, name='user_reservations'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
