from django.urls import path
from . import views


app_name='Doctor'


urlpatterns= [
    path('', views.view_doctor , name='view_doctor'),
    path('add/doctor' , views.add_doctor ,name='add_doctor'),
    path('delete/doctor/<id_doctor>/' , views.delete_doctor , name='delete_doctor'),
    path('update/doctor/<id_doctor>/' , views.update_doctor , name='update_doctor'),
]