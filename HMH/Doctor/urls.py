from django.urls import path
from . import views


app_name='Doctor'


urlpatterns= [
    path('', views.view_doctor , name='view_doctor'),
    path('add/doctor' , views.add_doctor ,name='add_doctor')
]