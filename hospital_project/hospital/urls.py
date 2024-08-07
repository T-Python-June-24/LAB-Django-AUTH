from django.urls import path
from . import views
from .views import LoginView, LogoutView, signup, edit_profile

urlpatterns = [
    path('', views.home, name='home'),
    path('clinics/', views.clinic_list, name='clinic-list'),
    path('clinics/<int:clinic_id>/', views.clinic_detail, name='clinic-detail'),
    path('clinics/create/', views.ClinicCreateView.as_view(), name='clinic-create'),
    path('clinics/<int:pk>/update/', views.ClinicUpdateView.as_view(), name='clinic-update'),
    path('clinics/<int:pk>/delete/', views.ClinicDeleteView.as_view(), name='clinic-delete'),

    path('doctors/', views.doctor_list, name='doctor-list'),
    path('doctors/<int:doctor_id>/', views.doctor_detail, name='doctor-detail'),
    path('doctors/create/', views.DoctorCreateView.as_view(), name='doctor-create'),
    path('doctors/<int:pk>/update/', views.DoctorUpdateView.as_view(), name='doctor-update'),
    path('doctors/<int:pk>/delete/', views.DoctorDeleteView.as_view(), name='doctor-delete'),

    path('staff-dashboard/', views.staff_dashboard, name='staff-dashboard'),

    path('profile/', views.profile, name='profile'),
    path('reservations/', views.reservations, name='reservations'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('profile/edit/',  edit_profile, name='edit_profile'),

]
