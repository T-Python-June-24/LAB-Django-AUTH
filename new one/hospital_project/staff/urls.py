from django.urls import path
from . import views

urlpatterns = [
    path('', views.staff_dashboard, name='staff_dashboard'),
    path('clinic/add/', views.add_clinic, name='add_clinic'),
    path('clinic/update/<int:pk>/', views.update_clinic, name='update_clinic'),
    path('clinic/delete/<int:pk>/', views.delete_clinic, name='delete_clinic'),
    path('doctor/add/', views.add_doctor, name='add_doctor'),
    path('doctor/update/<int:pk>/', views.update_doctor, name='update_doctor'),
    path('doctor/delete/<int:pk>/', views.delete_doctor, name='delete_doctor'),
]