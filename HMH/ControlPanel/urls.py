from django.urls import path
from . import views


app_name='ControlPanel'


urlpatterns= [
    path('', views.HomePanel , name='HomePanel'),
    path('login/admin/' , views.login_admin, name='login_admin'),
    path('view/doctor/' , views.view_doctor , name='view_doctor'),
    path('search/' , views.search , name='search'),
    path('view/clinic/' , views.view_clinic , name='view_clinic'),
    path('view/reservations/' , views.view_reservation , name='view_reservation')
    
]