from django.urls import path
from . import views

app_name = "doctors"

urlpatterns = [
  path('all/', views.doctors_list, name='doctors_list'),
  path('add/', views.add_doctor, name='add_doctor'),
  path('detail/<int:doctor_id>/', views.doctor_detail, name='doctor_detail'),
  path('update/<int:doctor_id>/', views.update_doctor, name='update_doctor'),
  path('delete/<int:doctor_id>/', views.delete_doctor, name='delete_doctor'),
]