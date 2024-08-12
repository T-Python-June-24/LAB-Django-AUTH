from django.urls import path
from . import views



app_name = 'reservations'



urlpatterns = [
    path('make/', views.make_reservation, name='make_reservation'),
    path('my/', views.user_reservations, name='user_reservations'),
    path('cancel/<int:pk>/', views.cancel_reservation, name='cancel_reservation'),
]
