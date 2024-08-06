from django.shortcuts import render
from django.http import HttpRequest
from Clinic.models import Clinic
from Doctor.models import Doctor

# Create your views here.


def Home(request:HttpRequest):
    clinic = Clinic.objects.all()
    doctor = Doctor.objects.all()
    return render(request, 'pages/index.html', 
                  {'clinic':clinic , 
                   'doctor':doctor
                   })