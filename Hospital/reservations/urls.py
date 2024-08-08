from django.urls import path
from . import views


app_name = "reservations"

urlpatterns = [
    path('select_clinic/', views.select_clinic, name='select_clinic'),
    path('select_doctor/<int:clinic_id>', views.select_doctor, name='select_doctor'),
    path("add/",views.make_reservation,name="make_reservation"),
    path("edit/<int:reservation_id>",views.edit_reservation,name="edit_reservation"),
    path("cancle/<int:reservation_id>",views.cancle_reservation,name="cancle_reservation")
]