from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Clinic
from .forms import ClinicForm
from django.contrib import messages
from doctors.models import Doctor
from django.core.paginator import Paginator


# Create your views here.
def create_clinic(request):
    doctors = Doctor.objects.all()
    if request.method == "POST":
        clinic_form = ClinicForm(request.POST, request.FILES)
        if clinic_form.is_valid():
            clinic_form.save()
            messages.success(request, 'Added clinic successfully!', 'alert-success')
            return redirect("clinics:all_clinics")
        else:
            messages.error(request, "Couldn't add clinic", "alert-danger")
    return render(request, "clinics/create_clinic.html", {'doctors': doctors})


def all_clinics(request):
    clinics = Clinic.objects.all()
    doctors = Doctor.objects.all()

    page_number = request.GET.get("page", 1)
    paginator = Paginator(clinics, 3)
    clinics = paginator.get_page(page_number)

    if request.user.is_staff:
        return render(request, "clinics/update_clinic.html", {"clinics": clinics, "doctors": doctors})
    else:
        return render(request, "clinics/all_clinics.html", {"clinics": clinics})


def clinic_details(request, clinic_id):
    clinic = Clinic.objects.get(pk=clinic_id)
    doctors = clinic.doctors.all()
    return render(request, "Clinics/clinic_details.html", {"clinic": clinic, "doctors": doctors})


def update_clinic(request, clinic_id):
    clinic = Clinic.objects.get(pk=clinic_id)
    doctors = Doctor.objects.all()
    if request.method == "POST":
        clinic_form = ClinicForm(request.POST, request.FILES, instance=clinic)
        if clinic_form.is_valid():
            clinic_form.save()
            messages.success(request, 'Updated clinic successfully!', "alert-success")
            return redirect('clinics:all_clinics')
        else:
            messages.error(request, "Couldn't update clinic", "alert-danger")
    return render(request, 'clinics/update_clinic.html',
                  {'clinic_form': clinic_form, 'clinic': clinic, 'doctors': doctors})


def delete_clinic(request, clinic_id):
    clinic = Clinic.objects.get(pk=clinic_id)
    if clinic.delete():
        messages.success(request, 'Deleted clinic successfully!', "alert-success")
        return redirect('clinics:all_clinics')
    else:
        messages.error(request, "Couldn't delete clinic", "alert-danger")
    return redirect('clinics:all_clinics')
