from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.core.paginator import Paginator
from .models import Clinic
from doctors.models import Doctor
from .forms import ClinicForm
from django.contrib import messages

def clinic_list(request):
    clinics = Clinic.objects.all()
    paginator = Paginator(clinics, 10) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    messages.info(request, f"Showing page {page_obj.number} of {paginator.num_pages}")
    return render(request, 'clinics/clinic_list.html', {'clinics': page_obj})

def clinic_detail(request, pk):
    clinic = get_object_or_404(Clinic, pk=pk)
    messages.info(request, f"You're viewing details for {clinic.name}")
    return render(request, 'clinics/clinic_detail.html', {'clinic': clinic})

@user_passes_test(lambda u: u.is_staff)
def add_clinic(request):
    if request.method == 'POST':
        form = ClinicForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Clinic added successfully!")
            return redirect('clinic_list')
        else:
            messages.error(request, "Failed to add clinic. Please correct the errors below.")
    else:
        form = ClinicForm()
    return render(request, 'clinics/add_clinic.html', {'form': form, 'doctors': Doctor.objects.all()})

@user_passes_test(lambda u: u.is_staff)
def edit_clinic(request, pk):
    clinic = get_object_or_404(Clinic, pk=pk)
    if request.method == 'POST':
        form = ClinicForm(request.POST, request.FILES, instance=clinic)
        if form.is_valid():
            form.save()
            messages.success(request, f"{clinic.name} updated successfully!")
            return redirect('clinic_detail', pk=clinic.pk)
        else:
            messages.error(request, "Failed to update clinic. Please correct the errors below.")
    else:
        form = ClinicForm(instance=clinic)
    return render(request, 'clinics/edit_clinic.html', {'form': form, 'clinic': clinic, 'doctors': Doctor.objects.all()})
