from django.urls import path
from . import views


app_name='Home'

urlpatterns = [
    path('' , views.Home , name='Home'),
    path('clinic/' , views.view_clinic , name='view_clinic'),
    path('doctor/' , views.view_doctor , name='view_doctor'),
    path('doctor/detail/<str:doctor_name>/', views.dector_detail , name='dector_detail'),
    path('clinic/detal/<clinic_name>/' , views.clinic_detail , name='clinic_detail'),
    path('profile/' , views.profile , name='profile'),
    path('search' , views.search , name='search'),
]