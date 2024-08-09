from django.shortcuts import render,redirect
from django.http import HttpRequest
from django.contrib import messages
from .models import Reservation
from doctor.models import Doctor
from clinic.models import Clinic
from datetime import datetime

def create_reservation(request:HttpRequest,clinic_id):
    if request.method == 'POST':
        user = request.user
        doctor_id = request.POST.get('doctor')
        date = request.POST.get('date')
        time_slot = request.POST.get('time_slot')
        clinic = Clinic.objects.get(pk=clinic_id)
        doctor = Doctor.objects.get(pk=doctor_id)
        try:
            reservation_datetime = datetime.strptime(f"{date} {time_slot}", '%Y-%m-%d %H:%M')
        except ValueError:
            messages.error(request, "Invalid date or time format.")
        if Reservation.objects.filter(clinic=clinic, doctor=doctor, date=date, time_slot=time_slot).exists():
            messages.error(request, "Sorry, the appointment is already reserved.", "red")
            return redirect('clinic:clinic_page', clinic_id=clinic_id)


        reservation = Reservation(
            user=user,
            clinic=clinic,
            doctor=doctor,
            date=date,
            time_slot=time_slot
        )
        try:
            reservation.save()
            messages.success(request, "Reservation created successfully.","green")
            return redirect('main:home_view')  # Redirect to a success page or wherever you want
        except Exception as e:
            messages.error(request, f"Error: {e}")
            return redirect('main:clinic_page', clinic_id=clinic_id)



def cancel_appointment(request: HttpRequest, reservation_id):
    try:
        print(reservation_id)
        reservation = Reservation.objects.get(pk=reservation_id)
        user = reservation.user.username
        reservation.delete()
        messages.success(request,"Deleted successfully.",'green')
        return redirect('registration:profile_view', user_name=user)
    except Reservation.DoesNotExist:
        # Handle the case where the reservation does not exist
        # You can redirect to a different page or show an error message
        return redirect('profile:profile_view', user_name=request.user.username) 