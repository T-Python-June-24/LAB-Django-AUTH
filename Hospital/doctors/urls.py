from django.urls import path
from . import views

app_name = 'doctors'

urlpatterns = [
    path('create/', views.create_doctor, name='create_doctor'),
    path('all/', views.all_doctors, name='all_doctors'),
    path('details/<int:doctor_id>/', views.doctor_details, name='doctor_details'),
    path('update/<int:doctor_id>/', views.update_doctor, name='update_doctor'),
    path('delete/<int:doctor_id>/', views.delete_doctor, name='delete_doctor'),

]
