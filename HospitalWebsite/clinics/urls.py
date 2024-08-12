from django.urls import path
from . import views


app_name = 'clinics'


urlpatterns = [
    path('', views.clinic_list, name='clinic_list'),
    path('<int:pk>/', views.clinic_detail, name='clinic_detail'),
    path('manage/', views.manage_clinics, name='manage_clinics'),
    path('manage/add/', views.clinic_create, name='clinic_create'),
    path('manage/<int:pk>/edit/', views.clinic_update, name='clinic_update'),
    path('manage/<int:pk>/delete/', views.clinic_delete, name='clinic_delete'),
]