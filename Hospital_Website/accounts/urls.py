# accounts/urls.py
from . import views
from django.urls import path

app_name = 'accounts'

urlpatterns = [
    path('', views.home, name='home'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('log_out/', views.log_out, name='log_out'),
    path('profile/', views.profile, name='profile'),
    path('profile/update', views.update_profile, name='update_profile'),
    path('<int:pk>/delete/', views.reservation_delete, name='reservation_delete'), 

]
