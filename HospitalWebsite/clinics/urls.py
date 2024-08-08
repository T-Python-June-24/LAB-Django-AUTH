from django.urls import path
from . import views

app_name = "clinics"

urlpatterns = [
  path('all/', views.clinics_list, name='clinics_list'),
  path('add/', views.add_clinic, name='add_clinic'),
  path('detail/<int:clinic_id>/', views.clinic_detail, name='clinic_detail'),
  path('update/<int:clinic_id>/', views.update_clinic, name='update_clinic'),
  path('delete/<int:clinic_id>/', views.delete_clinic, name='delete_clinic'),
]