from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Doctor
from .forms import DoctorForm
from django.contrib import messages
from doctors.models import Doctor
from django.core.paginator import Paginator


# Create your views here.
def create_doctor(request):
    if request.method == "POST":
        doctor_form = DoctorForm(request.POST, request.FILES)
        if doctor_form.is_valid():
            doctor_form.save()
            messages.success(request, 'Added doctor successfully!', 'alert-success')
            return redirect("doctors:all_doctors")
        else:
            messages.error(request, "Couldn't add doctor", "alert-danger")
    return render(request, "doctors/create_doctor.html", {'specialization': Doctor.Specialization.choices})


def all_doctors(request):
    doctors = Doctor.objects.all()

    page_number = request.GET.get("page", 1)
    paginator = Paginator(doctors, 3)
    doctors = paginator.get_page(page_number)

    if request.user.is_staff:
        return render(request, "doctors/update_doctor.html", {"doctors": doctors, "specialization": doctors})
    else:
        return render(request, "doctors/all_doctors.html", {"doctors": doctors})


def doctor_details(request, doctor_id):
    doctor = Doctor.objects.get(pk=doctor_id)
    return render(request, "doctors/doctor_details.html", {"doctor": doctor})


def update_doctor(request, doctor_id):
    doctor = Doctor.objects.get(pk=doctor_id)
    if request.method == "POST":
        doctor_form = DoctorForm(request.POST, request.FILES, instance=doctor)
        if doctor_form.is_valid():
            doctor_form.save()
            messages.success(request, 'Updated doctor successfully!', "alert-success")
            return redirect('doctors:all_doctors')
        else:
            messages.error(request, "Couldn't update doctor", "alert-danger")
    return render(request, 'doctors/update_doctor.html',
                  {'doctor_form': doctor_form, 'doctor': doctor, 'specialization': Doctor.Specialization.choices})


def delete_doctor(request, doctor_id):
    doctor = Doctor.objects.get(pk=doctor_id)
    if doctor.delete():
        messages.success(request, 'Deleted doctor successfully!', "alert-success")
        return redirect('doctors:all_doctors')
    else:
        messages.error(request, "Couldn't delete doctor", "alert-danger")
    return redirect('doctors:all_doctors')
