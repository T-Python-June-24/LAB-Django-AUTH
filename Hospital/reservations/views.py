from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .forms import ReservationForm
from django.contrib import messages

from .models import Clinic, Doctor

def select_clinic(request):
    clinics = Clinic.objects.all()
    return render(request, 'reservations/select_clinic.html', {'clinics': clinics})

def select_doctor(request):
    clinic_id = request.POST.get('clinic')
    clinic = Clinic.objects.get(id=clinic_id)
    doctors = Doctor.objects.filter(clinic=clinic)
    return render(request, 'reservations/select_details.html', {'clinic': clinic, 'doctors': doctors})

def make_reservation(request: HttpRequest):
    if request.method == "POST":
        reservationForm = ReservationForm(request.POST, request.FILES)
        if reservationForm.is_valid():
            reservationForm.save()
            messages.success(request, 'Doctor added successfully!', 'alert-success')
            return redirect("main:home")
        else:
            for field, errors in reservationForm.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}", 'alert-danger')
    else:
        reservationForm = ReservationForm()

    return render(request, "reservations/make_reservation.html", {'form': reservationForm})