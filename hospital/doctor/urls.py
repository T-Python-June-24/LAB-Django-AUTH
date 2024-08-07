from django.urls import path
from . import views
app_name='doctor'
urlpatterns = [
    path("page/<doctor_id>",views.doctor_page,name="doctor_page"),
    path("all/products",views.all_doctors_view,name="all_doctors_view"),
]