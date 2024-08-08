from django.urls import path
from . import views
app_name="clinic"
urlpatterns = [
    path('all/',views.all_clinic,name="all_clinic"),
    path('page/<clinic_id>',views.clinic_page,name="clinic_page"),
    
]