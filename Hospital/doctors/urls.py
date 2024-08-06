from django.urls import path
from . import views


app_name = "doctors"

urlpatterns = [
    path("",views.doctor_view,name="doctor_view"),
    path("add/",views.add_doctor,name="add_doctor"),
    path("update/<int:doctor_id>/", views.update_doctor, name="update_doctor"),
    path("delete/<int:doctor_id>/", views.delete_doctor, name="delete_doctor"),
]