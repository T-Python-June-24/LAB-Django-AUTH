from django.urls import path
from . import views

app_name = "reservations"

urlpatterns = [
  path('makereservation/', views.make_reservation, name='make_reservation'),
]