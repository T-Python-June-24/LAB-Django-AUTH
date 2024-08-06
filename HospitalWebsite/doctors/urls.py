from django.urls import path
from . import views

app_name = "doctors"

urlpatterns = [
  path('all/', views.doctors_list, name='doctors_list'),
  path('add/', views.add_doctor, name='add_doctor'),
  path('detail/<int:doctor_id>/', views.doctor_detail, name='doctor_detail'),
]