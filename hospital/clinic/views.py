from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

from django.contrib import messages

from .models import Clinic
from .forms import ClinicForm


# Create your views here.
def add_clinic(request:HttpRequest):

    if not (request.user.is_staff and request.user.has_perm("clinic.add_clinic")):
        messages.warning(request, "only staff can add Clinics", "alert-warning")
        return redirect("main:home")
    
    if request.method == "POST":

        clinic_form = ClinicForm(request.POST, request.FILES)

        if clinic_form.is_valid():
            clinic_form.save()
        else:
            print(clinic_form.errors)

        return redirect("clinic:clinic_page")

    return render(request, "clinic/add_clinic.html")


def clinics_list(request:HttpRequest):

    clinic = Clinic.objects.all()[:9]

    return render(request, "clinic/clinics_list.html", {"clinic" : clinic})


def clinic_page(request:HttpRequest, clinic_id):

    clinic = Clinic.objects.get(id=clinic_id)

    return render(request, "clinic/clinic_page.html", {"clinic" : clinic})
