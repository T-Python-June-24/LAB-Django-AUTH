from django.urls import path
from . import views


app_name ='Clinic'


urlpatterns = [
    path('' , views.view_clinic , name='view_clinic'),
    path('add/' , views.add_clinic , name='add_clinic'),
    path('delete/<id_clinic>/' , views.delete_clinic , name='delete_clinic'),
    path('update/<id_clinic>/' , views.update_doctor , name='update_doctor'),
]
