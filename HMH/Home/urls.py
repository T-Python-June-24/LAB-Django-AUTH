from django.urls import path
from . import views


app_name='Home'

urlpatterns = [
    path('' , views.Home , name='Home'),
    path('clinic/' , views.view_clinic , name='view_clinic'),
    path('doctor/' , views.view_doctor , name='view_doctor'),
    path('doctor/detail/', views.view_datail , name='view_datail')
]