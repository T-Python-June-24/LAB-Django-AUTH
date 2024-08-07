from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from doctors.models import Doctor
from .models import Clinic
from .forms import ClinicForm
from django.core.paginator import Paginator
from django.contrib import messages


def clinic_detail(request, pk):
    clinic = get_object_or_404(Clinic, pk=pk)
    other_clinics = Clinic.objects.all()
    return render(request, 'clinics/clinic_detail.html', {'clinic': clinic,'other_clinics': other_clinics})

def clinic_list(request):
    clinic_list = Clinic.objects.all()  
    paginator = Paginator(clinic_list, 10) 

    page_number = request.GET.get('page')
    clinics = paginator.get_page(page_number)
    return render(request, 'clinics/clinic_list.html', {'clinics': clinics})


def create_clinic(request):
    if request.user.is_staff:
        if request.method == 'POST':
            form = ClinicForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect(reverse('clinics:clinic_list'))
        else:
            form = ClinicForm()
    else:
        messages.error(request, 'You are not authorized to create a clinic')
        return redirect(reverse('clinics:clinic_list'))
        
    return render(request, 'clinics/clinic_form_create.html', {'form': form})

def update_clinic(request, pk):
    clinic = get_object_or_404(Clinic, pk=pk)
    if request.method == 'POST':
        form = ClinicForm(request.POST, request.FILES, instance=clinic)
        if form.is_valid():
            form.save()
            return redirect(reverse('clinics:clinic_list'))
    else:
        form = ClinicForm(instance=clinic)
    
    return render(request, 'clinics/clinic_form_update.html', {'form': form})

def clinic_delete(request, pk):
    clinic = get_object_or_404(Clinic, pk=pk)
    if request.method == 'POST':
        clinic.delete()
        return redirect('clinics:clinic_list')  
    return render(request, 'clinics/clinic_confirm_delete.html', {'clinic': clinic})
