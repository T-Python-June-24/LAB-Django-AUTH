from django.shortcuts import render
from django.http import HttpRequest
from .models import Doctor
# Create your views here.
def doctor_page(request:HttpRequest,doctor_id)->render:
    doctor=Doctor.objects.get(pk=doctor_id)
    return render(request,"doctor/doctor_page.html",{"doctor":doctor})
def all_doctors_view(request:HttpRequest):
    doctors=Doctor.objects.all()
    return render(request,"doctor/all_doctors.html",{"doctors":doctors})