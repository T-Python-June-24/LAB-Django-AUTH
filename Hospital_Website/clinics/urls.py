from django.urls import path
from . import views

app_name = 'clinics'

urlpatterns = [
    path('create/', views.create_clinic, name='clinic_create'),
    path('<int:pk>/update/', views.update_clinic, name='clinic_update'),
    path('', views.clinic_list, name='clinic_list'),  # Ensure this matches the view name
        path('<int:pk>/', views.clinic_detail, name='clinic_detail'),  # Add this line
            path('<int:pk>/delete/', views.clinic_delete, name='clinic_delete'),


]
