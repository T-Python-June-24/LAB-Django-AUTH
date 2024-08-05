# clinic/urls.py
from django.urls import path
from . import views

app_name = 'clinics'

urlpatterns = [
    path('', views.clinic_list, name='clinic_list'),
    path('<int:pk>/', views.clinic_detail, name='clinic_detail'),
    path('create/', views.clinic_create, name='clinic_create'),
    path('<int:pk>/update/', views.clinic_update, name='clinic_update'),
]
