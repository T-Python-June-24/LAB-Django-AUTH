from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import transaction, IntegrityError
from .models import Clinic, Doctor, Reservation
from django.http import HttpRequest
# Create your views here.


def make_reservation(request: HttpRequest):
    if not request.user.is_authenticated:
        return redirect('accounts:sign_in')

    if request.method == "POST":
        clinic_id = request.POST.get('clinic')
        doctor_id = request.POST.get('doctor')
        date = request.POST.get('date')
        time_slot = request.POST.get('time_slot')

        # Check if reservation already exists
        if Reservation.objects.filter(user=request.user, date=date, time_slot=time_slot).exists():
            messages.error(request, "You already have a reservation for this time slot.")
            return render(request, 'reservations/make_reservation.html', {'clinics': Clinic.objects.all(), 'doctors': Doctor.objects.all(), 'time_slots': Reservation.TIME_SLOT_CHOICES})

        # Create a new reservation
        Reservation.objects.create(
            user=request.user,
            clinic_id=clinic_id,
            doctor_id=doctor_id,
            date=date,
            time_slot=time_slot
        )
        messages.success(request, "Reservation made successfully!")
        return redirect('clinics:clinics_list')
    
    clinics = Clinic.objects.all()
    doctors = Doctor.objects.all()
    time_slots = Reservation.TIME_SLOT_CHOICES

    return render(request, 'reservations/make_reservation.html', {'clinics': clinics, 'doctors': doctors, 'time_slots': time_slots})
