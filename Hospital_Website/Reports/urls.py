from . import views
from django.urls import path

app_name = 'Reports'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
]