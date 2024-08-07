from django.urls import path
from . import views

urlpatterns = [
    path('', views.reservation_list, name='reservation_list'),
    path('create/', views.create_reservation, name='create_reservation'),
    path('<int:pk>/', views.reservation_detail, name='reservation_detail'),
    path('<int:pk>/cancel/', views.cancel_reservation, name='cancel_reservation'),
    path('get-doctors/<int:clinic_id>/', views.get_doctors, name='get_doctors'),
]
