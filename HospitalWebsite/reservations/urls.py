from django.urls import path
from . import views

app_name = "reservations"

urlpatterns = [
  path('makereservation/', views.make_reservation, name='make_reservation'),
  path('deletereservation/<int:reservation_id>/', views.delete_reservation, name='delete_reservation'),
  path('reservations/', views.user_reservations, name='user_reservations'),
]