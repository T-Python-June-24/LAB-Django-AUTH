from django.urls import path
from . import views

app_name = "patientSummary"
urlpatterns = [
    path("add/patient/summary/<appointment_id>" ,views.add_patient_summary, name="add_patient_summary"),
    path("patient/summary/<patient_id>" ,views.display_patient_summary, name="display_patient_summary"),
    path("all/patient/summary/" ,views.all_patient_summary, name="all_patient_summary"),
]