from django.urls import path
from . import views

app_name = "reservations"

urlpatterns = [
    path("create", views.create, name="create_reservation"),
    path("reservation/page", views.reservation_page, name="reservation_page"),
]