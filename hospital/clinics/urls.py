from django.urls import path
from . import views

app_name = "clinics"

urlpatterns = [
    path("",views.clinic_view,name="clinic_view"),
    path("add/",views.add_clinic,name="add_clinic"),
    path("update/<int:clinic_id>/",views.update_clinic,name="update_clinic"),
    path("delete/<int:clinic_id>/",views.delete_clinic,name="delete_clinic"),
    path("detail/<int:clinic_id>/",views.clinic_detail,name="clinic_detail"),

]