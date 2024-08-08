from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .forms import ReservationForm
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from .models import Clinic, Doctor,Reservation,Profile
from django.db import transaction

def select_clinic(request:HttpRequest):
    if not request.user.is_authenticated:
        messages.error(request, "You need to be logged in to make a reservation", "alert-danger")
        return redirect("profiles:sign_in")    
    clinics = Clinic.objects.all()
    return render(request, 'reservations/select_clinic.html', {'clinics': clinics})

def select_doctor(request:HttpRequest,clinic_id):
    if not request.user.is_authenticated:
        messages.error(request, "You need to be logged in to make a reservation", "alert-danger")
        return redirect("profiles:sign_in")
    clinic = Clinic.objects.get(pk=clinic_id)
    doctors = Doctor.objects.filter(clinic=clinic)
    return render(request, 'reservations/select_details.html', {'clinic': clinic, 'doctors': doctors})




def make_reservation(request):
    if not request.user.is_authenticated:
        messages.error(request, "You need to be logged in to make a reservation", "alert-danger")
        return redirect("profiles:sign_in")
    
    # getting the user entries from teh selcet doctor view 
    if request.method == "POST":
        user_profile = Profile.objects.get(user=request.user)
        clinic_id = request.POST.get("clinic")
        doctor_id = request.POST.get("doctor")
        time_slot = request.POST.get("time_slot")
        date = request.POST.get("date")

        # creating clinc and doctor instance based on the user entries (by the id)
        clinic_instance = Clinic.objects.get(id=clinic_id)
        doctor_instance = Doctor.objects.get(id=doctor_id)

        # Check if  existing reservation as the user entries 
        existing_reservation = Reservation.objects.filter(
            clinic=clinic_instance,
            doctor=doctor_instance,
            time_slot=time_slot,
            date=date
        ).exists()

        if existing_reservation:
            messages.error(request, "Unavailable. Try another date or doctor.", "alert-danger")
            return redirect("reservations:select_doctor",clinic_id)

        # If no existing reservation, then add new one to create a new one
        with transaction.atomic():
            new_reservation = Reservation(
                user=user_profile, 
                time_slot=time_slot,
                date=date,  
                clinic=clinic_instance,  
                doctor=doctor_instance,  
            )
            new_reservation.save()
            messages.success(request, "Reservation made successfully!", "alert-success")
            return redirect("main:home_view")

    return render(request, "reservations/make_reservation.html")

def edit_reservation(request, reservation_id):
    reservation = Reservation.objects.get(pk=reservation_id) 
    clinic = reservation.clinic  
    doctors = Doctor.objects.filter(clinic=clinic)
    
    if request.method == 'POST':
        user_profile = Profile.objects.get(user=request.user)
        doctor_id = request.POST.get("doctor")  
        doctor = Doctor.objects.get(id=doctor_id)  

        reservation.user = user_profile
        reservation.time_slot = request.POST.get("time_slot")
        reservation.date = request.POST.get("date")
        reservation.doctor = doctor  
      
        existing_reservation = Reservation.objects.filter(
            clinic=clinic,
            doctor=doctor,
            time_slot=reservation.time_slot,
            date=reservation.date
        ).exists()

        if existing_reservation:
            messages.error(request, "Unavailable. Try another date or doctor.", "alert-danger")
            return redirect("profiles:user_profile_view",user_name=user_profile.user.username)

        # If no existing reservation, then add new one to create a new one
        with transaction.atomic():
            reservation.user = reservation.user
            reservation.doctor = reservation.doctor
            reservation.time_slot = reservation.time_slot
            reservation.date = reservation.date
            reservation.save()

        messages.success(request, 'Reservation updated successfully!', 'alert-success')
        return redirect('profiles:user_profile_view', user_name=user_profile.user.username)

    return render(request, 'profiles/profile.html', {
        'reservation': reservation,
        'clinic': clinic,
        'doctors': doctors,
    })


def cancle_reservation(request,reservation_id):
    user_profile = Profile.objects.get(user=request.user)
    reservation=Reservation.objects.get(pk=reservation_id)
    if reservation.delete():
             messages.success(request, 'your reservation canceld successfully!',"alert-success")
             return redirect('profiles:user_profile_view', user_name=user_profile.user.username)
    else:
         for field, errors in reservation.errors.items():
             for error in errors:
                 messages.error(request, f"{field}: {error}","alert-danger")    
             return redirect('profiles:user_profile_view', user_name=user_profile.user.username)

