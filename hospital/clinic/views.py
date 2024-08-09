from django.shortcuts import render
from django.http import HttpRequest
from .models import Clinic
from django.shortcuts import render, get_object_or_404
from datetime import datetime, timedelta

def get_available_time_slots(clinic, date):
    working_hours = clinic.get_working_hours()
    day_of_week = date.strftime('%A')

    if day_of_week not in working_hours:
        return []

    start_time_str, end_time_str = working_hours[day_of_week]
    start_time = datetime.strptime(start_time_str, '%H:%M').time()
    end_time = datetime.strptime(end_time_str, '%H:%M').time()

    time_slots = []
    current_time = datetime.combine(date, start_time)
    end_datetime = datetime.combine(date, end_time)

    while current_time <= end_datetime:
        time_slots.append(current_time.strftime('%H:%M'))
        current_time += timedelta(hours=1)

    return time_slots
def clinic_page(request:HttpRequest,clinic_id):
    clinic=Clinic.objects.get(pk=clinic_id)
    date = datetime.now().date()
    time_slots = get_available_time_slots(clinic, date)
    
    return render(request,"clinic/clinic_page.html",{"clinic":clinic, "time_slots": time_slots,"today":datetime.now().date().isoformat()})
def all_clinic(request:HttpRequest):
    clinics=Clinic.objects.all()
    return render(request,"clinic/all_clinic.html",{"clinics":clinics})
