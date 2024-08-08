from django.urls import path
from . import views

app_name = "clinic"

urlpatterns = [
    path("add", views.add_clinic, name="add_clinic"),
    path("all/clinics/", views.clinics_list, name="clinics_list"),
    path("<clinic_id>/", views.clinic_page, name="clinic_page"),
]