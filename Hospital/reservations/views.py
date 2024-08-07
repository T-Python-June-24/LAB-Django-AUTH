from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .forms import ReservationForm
from django.contrib import messages

from .models import Clinic, Doctor,Reservation,Profile

def select_clinic(request:HttpRequest):
    clinics = Clinic.objects.all()
    return render(request, 'reservations/select_clinic.html', {'clinics': clinics})

def select_doctor(request:HttpRequest,clinic_id):
    clinic = Clinic.objects.get(pk=clinic_id)
    doctors = Doctor.objects.filter(clinic=clinic)
    return render(request, 'reservations/select_details.html', {'clinic': clinic, 'doctors': doctors})


def make_reservation(request:HttpRequest):
    if not request.user.is_authenticated:
        messages.error(request, "You need to be logged in to make a reservation", "alert-danger")
        return redirect("accounts:sign_in")

    if request.method == "POST":
        user_profile = Profile.objects.get(user=request.user)

       
        clinic_id = request.POST.get("clinic")
        clinic_instance = Clinic.objects.get(id=clinic_id)

        doctor_id=request.POST.get("doctor")
        doctor_instance = Doctor.objects.get(id=doctor_id)

        new_reservation = Reservation(
            user=user_profile, 
            time_slot=request.POST.get("time_slot"),
            date=request.POST.get("date"),  
            clinic=clinic_instance,  
            doctor=doctor_instance,  
        )
        new_reservation.save()

        messages.success(request, "Reservation made successfully!", "alert-success")
        return redirect("main:home_view")

    return render(request, "reservations/make_reservation.html")