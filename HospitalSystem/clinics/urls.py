from django.urls import path
from . import views

app_name = "clinics"

urlpatterns = [

    path('', views.all_clinics, name="all_clinics"),
    path('add/', views.add_clinic, name="add_clinic"),
    path('delete/<int:clinic_id>', views.delete_clinic, name="delete_clinic"),
    path('update/<int:clinic_id>', views.update_clinic, name="update_clinic"),


]

