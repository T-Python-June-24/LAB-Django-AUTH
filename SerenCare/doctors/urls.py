from django.urls import path
from . import views

app_name = "doctors"

urlpatterns = [
    path("doctors/<doctor_id>/",views.all_doctors_view,name="all_doctors_view"),
    path('doctor_detail/<doctor_id>/', views.doctor_detail_view, name='doctor_detail_view'),

]