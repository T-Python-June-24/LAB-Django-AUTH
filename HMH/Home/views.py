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
    
def view_clinic(request:HttpRequest):
    clinic = Clinic.objects.all()
    return render(request , 'pages/clinic_page.html' , {'clinic':clinic})

def view_doctor(request:HttpRequest):
    doctor = Doctor.objects.all()
    return render(request , 'pages/doctor_page.html' , {'doctor':doctor})

def view_datail(request:HttpRequest):
    return render(request , 'pages/doctor_Detail.html')