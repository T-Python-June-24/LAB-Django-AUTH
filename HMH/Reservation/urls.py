from django.urls import path
from . import views


app_name='Reservation'


urlpatterns= [
    path('add_reservation/<clinic_name>', views.add_reservation , name='add_reservation'),
    path('delete/reservations/<id_reservation>/' , views.delete_reservation , name='delete_reservation'),
 

]