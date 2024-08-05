from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('staff/', views.staff_dashboard, name='staff_dashboard'),
    path('search/', views.search, name='search'),
]
