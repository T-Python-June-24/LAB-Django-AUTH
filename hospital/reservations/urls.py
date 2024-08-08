from django.urls import path
from . import views

app_name = "reservations"

urlpatterns = [
    path("add/", views.add_reservation, name="add_reservation"),
    path("", views.reservation_list, name="reservation_list"),
    path("create/", views.add_reservation, name="add_reservation"),
    path("update/<int:pk>/", views.reservation_update, name="reservation_update"),
    path("delete/<int:pk>/", views.reservation_delete, name="reservation_delete"),
]