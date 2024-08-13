from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
  path('signup/', views.sign_up, name='sign_up'),
  path('signin/', views.sign_in, name='sign_in'),
  path('logout/', views.log_out, name='log_out'),
  path('profile/', views.profile_view, name='profile'),
  path('profile/edit/', views.edit_profile_view, name='edit_profile'),
]