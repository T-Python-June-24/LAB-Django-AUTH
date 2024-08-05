
from django.urls import path
from . import views


urlpatterns = [
    path('', views.doctor_list, name='doctor_list'),
    path('<int:pk>/', views.doctor_detail, name='doctor_detail'),
    path('add/', views.add_doctor, name='add_doctor'),
    path('<int:pk>/edit/', views.edit_doctor, name='edit_doctor'),
]
