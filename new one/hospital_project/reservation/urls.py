# reservation/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.reservation_list, name='reservation_list'),
    path('<int:pk>/', views.reservation_detail, name='reservation_detail'),
    path('<int:pk>/cancel/', views.reservation_cancel, name='reservation_cancel'),
    path('create/', views.create_reservation, name='create_reservation'),
    path('get_doctors_for_clinic/<int:clinic_id>/', views.get_doctors_for_clinic, name='get_doctors_for_clinic'),
    
    
    path('cancel/<int:pk>/', views.reservation_cancel, name='reservation_cancel'),
    path('get_working_hours_for_clinic/<int:clinic_id>/', views.get_working_hours_for_clinic, name='get_working_hours_for_clinic'),
]