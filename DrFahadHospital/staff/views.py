from django.shortcuts import render, redirect
from clinic.forms import ClinicForm
from doctor.forms import DoctorForm

def dashboard(request):
    return render(request, 'staff/dashboard.html')

def clinic_create(request):
    if request.method == 'POST':
        form = ClinicForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ClinicForm()
    return render(request, 'staff/clinic_form.html', {'form': form})

def doctor_create(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = DoctorForm()
    return render(request, 'staff/doctor_form.html', {'form': form})