from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test
from clinic.models import Clinic
from doctor.models import Doctor
from .forms import ClinicForm, DoctorForm

@user_passes_test(lambda u: u.is_staff)
def staff_dashboard(request):
    print(f"Rendering template: staff/dashboard.html")
    clinics = Clinic.objects.all()
    doctors = Doctor.objects.all()
    return render(request, 'staff/dashboard.html', {'clinics': clinics, 'doctors': doctors})

@user_passes_test(lambda u: u.is_staff)
def add_clinic(request):
    if request.method == 'POST':
        form = ClinicForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('staff_dashboard')
    else:
        form = ClinicForm()
    return render(request, 'staff/add_clinic.html', {'form': form})

@user_passes_test(lambda u: u.is_staff)
def update_clinic(request, pk):
    clinic = get_object_or_404(Clinic, pk=pk)
    if request.method == 'POST':
        form = ClinicForm(request.POST, request.FILES, instance=clinic)
        if form.is_valid():
            form.save()
            return redirect('staff_dashboard')
    else:
        form = ClinicForm(instance=clinic)
    return render(request, 'staff/update_clinic.html', {'form': form})

@user_passes_test(lambda u: u.is_staff)
def delete_clinic(request, pk):
    clinic = get_object_or_404(Clinic, pk=pk)
    if request.method == 'POST':
        clinic.delete()
        return redirect('staff_dashboard')
    return render(request, 'staff/delete_clinic.html', {'clinic': clinic})

@user_passes_test(lambda u: u.is_staff)
def add_doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('staff_dashboard')
    else:
        form = DoctorForm()
    return render(request, 'staff/add_doctor.html', {'form': form})

@user_passes_test(lambda u: u.is_staff)
def update_doctor(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        form = DoctorForm(request.POST, request.FILES, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('staff_dashboard')
    else:
        form = DoctorForm(instance=doctor)
    return render(request, 'staff/update_doctor.html', {'form': form})

@user_passes_test(lambda u: u.is_staff)
def delete_doctor(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        doctor.delete()
        return redirect('staff_dashboard')
    return render(request, 'staff/delete_doctor.html', {'doctor': doctor})