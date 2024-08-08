from django.shortcuts import render, redirect
from django.http import HttpRequest
from clinics.models import Clinic
from doctors.models import Doctor
from django.contrib import messages


# Create your views here.
def home_view(request: HttpRequest):
  clinics = Clinic.objects.all()[:3]  
  doctors = Doctor.objects.all()[:3]  
  return render(request, 'main/home.html', {'clinics': clinics, 'doctors': doctors})


def staff_dashboard(request: HttpRequest):
    if not request.user.is_authenticated and not request.user.is_staff:
        messages.error(request, 'You do not have permission to access this page.')
        return redirect('main:home_view')

    return render(request, 'main/dashboard.html')


def staff_dashboard(request: HttpRequest):
    if request.user.is_authenticated and request.user.is_staff:
        doctors = Doctor.objects.all()
        clinics = Clinic.objects.all()
        return render(request, 'main/dashboard.html', {'doctors': doctors, 'clinics': clinics})
    return redirect('main:home_view') 