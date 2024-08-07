from django.urls import path
from .views import ReservationListView, ReservationCreateView

urlpatterns = [
    path('', ReservationListView.as_view(), name='reservations'),
    path('new/', ReservationCreateView.as_view(), name='reservation_add'),
]
