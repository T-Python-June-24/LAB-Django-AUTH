from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from clinic.models import Clinic
from doctor.models import Doctor

def home_view(request:HttpRequest):
        clinic = Clinic.objects.prefetch_related('doctors_id').all()
        return render(request, "index.html",{"clinics":clinic})

def details_clinics(request: HttpRequest, clinic_id):
    clinic = Clinic.objects.get(id=clinic_id)

    return render(request, "clinic_details.html", {"clinic":clinic})

@login_required(login_url="account:log_in")
def dashboard_view(request:HttpRequest):

    return render(request, "dashboard.html")