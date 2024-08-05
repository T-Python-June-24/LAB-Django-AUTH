from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.core.paginator import Paginator
from .models import Doctor
from clinics.models import Clinic
from .forms import DoctorForm
from django.contrib import messages

def doctor_list(request):
    doctors = Doctor.objects.all()
    paginator = Paginator(doctors, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    messages.info(request, f"Showing page {page_obj.number} of {paginator.num_pages}")
    return render(request, 'doctors/doctor_list.html', {'doctors': page_obj})

def doctor_detail(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    messages.info(request, f"You're viewing details for Dr. {doctor.full_name}")
    return render(request, 'doctors/doctor_detail.html', {'doctor': doctor})

@user_passes_test(lambda u: u.is_staff)
def add_doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Doctor added successfully!")
            return redirect('doctor_list')
        else:
            messages.error(request, "Failed to add doctor. Please correct the errors below.")
    else:
        form = DoctorForm()
    return render(request, 'doctors/add_doctor.html', {
        'form': form,
        'clinics': Clinic.objects.all(),
        'specializations': Doctor.SPECIALIZATION_CHOICES
    })

@user_passes_test(lambda u: u.is_staff)
def edit_doctor(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        form = DoctorForm(request.POST, request.FILES, instance=doctor)
        if form.is_valid():
            form.save()
            messages.success(request, f"Dr. {doctor.full_name}'s information updated successfully!")
            return redirect('doctor_detail', pk=doctor.pk)
        else:
            messages.error(request, "Failed to update doctor information. Please correct the errors below.")
    else:
        form = DoctorForm(instance=doctor)
    return render(request, 'doctors/edit_doctor.html', {
        'form': form,
        'doctor': doctor,
        'clinics': Clinic.objects.all(),
        'specializations': Doctor.SPECIALIZATION_CHOICES
    })
