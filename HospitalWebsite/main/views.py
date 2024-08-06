from django.shortcuts import render
from django.http import HttpRequest
from clinics.models import Clinic
from doctors.models import Doctor


# Create your views here.
def home_view(request: HttpRequest):
  clinics = Clinic.objects.all()[:3]  
  doctors = Doctor.objects.all()[:3]  
  return render(request, 'main/home.html', {'clinics': clinics, 'doctors': doctors})
