from django.urls import path
from . import views

app_name = 'clinics'

urlpatterns = [
    path('create/', views.create_clinic, name='create_clinic'),
    path('all/', views.all_clinics, name='all_clinics'),
    path('details/<int:clinic_id>/', views.clinic_details, name='clinic_details'),
    path('update/<int:clinic_id>/', views.update_clinic, name='update_clinic'),
    path('delete/<int:clinic_id>/', views.delete_clinic, name='delete_clinic'),

]
