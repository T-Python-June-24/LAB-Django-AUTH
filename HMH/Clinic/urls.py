from django.urls import path
from . import views


app_naem = 'Cllinic'


urlpatterns = [
    path('' , views.view_clinic , name='view_clinic'),
]
