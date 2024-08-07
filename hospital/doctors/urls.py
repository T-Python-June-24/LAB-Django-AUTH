from django.urls import path
from . import views

app_name = "doctors"

urlpatterns = [
    path("add", views.add_doctor, name="add_doctor"),
    path("all/doctors/", views.doctors_list, name="doctors_list"),
    path("<doctor_id>/", views.doctor_page, name="doctor_page"),
]