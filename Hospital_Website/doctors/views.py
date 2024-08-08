from django.shortcuts import render, redirect,get_object_or_404

from clinics.models import Clinic
from .models import Doctor
from .forms import DoctorForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import  Doctor
from .forms import SearchForm

def search(request):
    query = request.GET.get('query', '')
    clinics_list = Clinic.objects.filter(name__icontains=query)
    doctors_list = Doctor.objects.filter(full_name__icontains=query)
    
    clinic_paginator = Paginator(clinics_list, 5)  
    doctor_paginator = Paginator(doctors_list, 5)  

    clinic_page_number = request.GET.get('clinic_page')
    doctor_page_number = request.GET.get('doctor_page')

    clinics = clinic_paginator.get_page(clinic_page_number)
    doctors = doctor_paginator.get_page(doctor_page_number)

    form = SearchForm(request.GET)

    context = {
        'form': form,
        'clinics': clinics,
        'doctors': doctors,
        'query': query,
    }

    return render(request, 'doctors/search_results.html', context)

def doctor_list(request):
    doctors = Doctor.objects.all()
    
    paginator = Paginator(doctors, 8)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'doctors': doctors,
            }
    
    return render(request, 'doctors/doctor_list.html', context)


def doctor_detail(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    return render(request, 'doctors/doctor_detail.html', {'doctor': doctor})


def doctor_create(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('doctors:doctor_list')
    else:
        form = DoctorForm()

    specializations = Doctor.SPECIALIZATIONS
    return render(request, 'doctors/doctor_form.html', {'form': form, 'specializations': specializations})

@login_required
def doctor_update(request, pk):
    doctor = Doctor.objects.get(pk=pk)
    if request.method == 'POST':
        form = DoctorForm(request.POST, request.FILES, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('doctors:doctor_list')
    else:
        form = DoctorForm(instance=doctor)
        
        
    specializations = Doctor.SPECIALIZATIONS

    return render(request, 'doctors/doctor_update.html', {'form': form, 'specializations': specializations})

@login_required
def doctor_delete(request, pk):
    doctor = Doctor.objects.get(pk=pk)
    if request.method == 'POST':
        doctor.delete()
        return redirect('doctors:doctor_list')
    return render(request, 'doctors/doctor_confirm_delete.html', {'doctor': doctor})
