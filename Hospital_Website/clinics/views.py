from django.shortcuts import render, get_object_or_404, redirect
from .models import Clinic
from .forms import ClinicForm

def clinic_list(request):
    clinics = Clinic.objects.all()
    return render(request, 'clinics/clinic_list.html', {'clinics': clinics})

def clinic_detail(request, pk):
    clinic = get_object_or_404(Clinic, pk=pk)
    return render(request, 'clinics/clinic_detail.html', {'clinic': clinic})

def clinic_create(request):
    if request.method == 'POST':
        form = ClinicForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('clinics:clinic_list')
    else:
        form = ClinicForm()
    return render(request, 'clinics/clinic_form.html', {'form': form})

def clinic_update(request, pk):
    clinic = get_object_or_404(Clinic, pk=pk)
    if request.method == 'POST':
        form = ClinicForm(request.POST, request.FILES, instance=clinic)
        if form.is_valid():
            form.save()
            return redirect('clinics:clinic_detail', pk=clinic.pk)
    else:
        form = ClinicForm(instance=clinic)
    return render(request, 'clinics/clinic_form.html', {'form': form})
