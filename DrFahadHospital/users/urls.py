from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import register, login_view, profile

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('profile/', profile, name='profile'),
]
