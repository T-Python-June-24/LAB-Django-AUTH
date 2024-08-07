from django.urls import path
from . import views

urlpatterns = [
    path('', views.clinic_list, name='clinic_list'),
    path('<int:pk>/', views.clinic_detail, name='clinic_detail'),
    path('add/', views.add_clinic, name='add_clinic'),
    path('<int:pk>/edit/', views.edit_clinic, name='edit_clinic'),
]
