from django.urls import path
from . import views

app_name = "patientSummary"
urlpatterns = [
    path("add/patient/summary/" ,views.add_patient_summary, name="add_patient_summary"),
    path("patient/summary/" ,views.display_patient_summary, name="display_patient_summary"),
]