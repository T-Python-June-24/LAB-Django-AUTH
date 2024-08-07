from django.urls import path
from . import views


app_name = "reservations"

urlpatterns = [
    path('select_clinic/', views.select_clinic, name='select_clinic'),
    path('select_doctor/', views.select_doctor, name='select_doctor'),
    path("add/",views.make_reservation,name="make_reservation"),

]