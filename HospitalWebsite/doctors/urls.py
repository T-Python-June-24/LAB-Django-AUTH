from django.urls import path
from . import views


app_name = 'doctors'


urlpatterns = [
    path('', views.doctor_list, name='doctor_list'),
    path('<int:pk>/', views.doctor_detail, name='doctor_detail'),
    path('manage/', views.manage_doctors, name='manage_doctors'),
    path('manage/add/', views.doctor_create, name='doctor_create'),
    path('manage/<int:pk>/edit/', views.doctor_update, name='doctor_update'),
    path('manage/<int:pk>/delete/', views.doctor_delete, name='doctor_delete'),
]
