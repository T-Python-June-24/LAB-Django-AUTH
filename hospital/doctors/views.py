from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

from django.contrib import messages

from .models import Doctor
from .forms import DoctorForm


# Create your views here.
def add_doctor(request:HttpRequest):

    if not (request.user.is_staff and request.user.has_perm("doctor.add_doctor")):
        messages.warning(request, "only staff can add doctors", "alert-warning")
        return redirect("main:home")
    
    if request.method == "POST":

        doctor_form = DoctorForm(request.POST, request.FILES)

        if doctor_form.is_valid():
            doctor_form.save()
        else:
            print(doctor_form.errors)

        return redirect("doctor:doctor_page")

    return render(request, "doctor/add_doctor.html")


def doctors_list(request:HttpRequest):

    doctor = Doctor.objects.all()[:9]

    return render(request, "doctor/doctors_list.html", {"doctor" : doctor})


def doctor_page(request:HttpRequest, doctor_id):

    doctor = Doctor.objects.get(id=doctor_id)

    return render(request, "doctor/doctor_page.html", {"doctor" : doctor})
