# clinic/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.clinic_list, name='clinic_list'),
    path('<int:pk>/', views.clinic_detail, name='clinic_detail'),
]