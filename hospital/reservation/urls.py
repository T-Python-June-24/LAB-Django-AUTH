from django.urls import path
from . import views
app_name="reservation"
urlpatterns = [
    path("create/<clinic_id>",views.create_reservation,name="create_reservation"),
]