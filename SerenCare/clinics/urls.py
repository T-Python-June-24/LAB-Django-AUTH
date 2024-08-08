from django.urls import path
from . import views

app_name = "clinics"

urlpatterns = [
    path("all_clinics/<clinic_id>/", views.all_clinics_view, name="all_clinics_view"),
    path('clinic_detail/<clinic_id>/', views.clinic_detail_view, name='clinic_detail_view'),
    path("delete_clinic/<clinic_id>/", views.delete_clinic_view, name="delete_clinic_view"),
    path("reservation/", views.reservation_view, name="reservation_view"),
    path("search/", views.search_clinics_view, name="search_clinics_view"),
]
