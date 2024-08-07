from django.urls import path
from . import views
from .views import LoginView, LogoutView, signup

urlpatterns = [
    path('', views.home, name='home'),
    path('clinics/', views.clinic_list, name='clinic-list'),
    path('clinics/<int:clinic_id>/', views.clinic_detail, name='clinic-detail'),
    path('doctors/', views.doctor_list, name='doctor-list'),
    path('doctors/<int:doctor_id>/', views.doctor_detail, name='doctor-detail'),
    path('profile/', views.profile, name='profile'),
    path('reservations/', views.reservations, name='reservations'),
    path('staff-dashboard/', views.staff_dashboard, name='staff-dashboard'),
    path('doctors/create/', views.DoctorCreateView.as_view(), name='doctor-create'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),

]
