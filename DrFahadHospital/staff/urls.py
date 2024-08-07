from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('clinic/new/', views.clinic_create, name='clinic_create'),
    path('doctor/new/', views.doctor_create, name='doctor_create'),
]