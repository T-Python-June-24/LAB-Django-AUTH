from django.urls import path
from . import views
app_name="main"
urlpatterns = [
    path("",views.home_view,name="home_view"),
    path("sttaf/dashboard",views.sttaf_view,name="sttaf_view"),
    path('add/doctor',views.add_doctor_view,name="add_doctor_view"),
    path('add/clinic',views.add_clinic_view,name="add_clinic_view"),
    
]