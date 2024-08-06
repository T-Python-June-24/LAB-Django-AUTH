from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.core.paginator import Paginator
from clinics.models import Clinic
from django.contrib import messages
from doctors.models import Doctor

# Create your views here.

def clinics_list(request: HttpRequest):
    clinic_list = Clinic.objects.all()
    paginator = Paginator(clinic_list, 5) 
    page_number = request.GET.get('page')
    clinics = paginator.get_page(page_number)
    return render(request, 'clinics/clinics_list.html', {'clinics': clinics})


def clinic_detail(request: HttpRequest, clinic_id: int):
    clinic = Clinic.objects.get(pk=clinic_id)
    return render(request, 'clinics/clinic_detail.html', {'clinic': clinic})


def add_clinic(request: HttpRequest):
  doctors = Doctor.objects.all()  
  if request.method == 'POST':
    name = request.POST.get('name')
    description = request.POST.get('description')
    working_hours = request.POST.get('working_hours')
    feature_image = request.FILES.get('feature_image')
    selected_doctors = request.POST.getlist('doctors')  

    if name and description and working_hours and feature_image:
      clinic = Clinic(
        name=name,
        description=description,
        working_hours=working_hours,
        feature_image=feature_image
      )
      clinic.save()
      clinic.doctors.set(selected_doctors)
      messages.success(request, 'Clinic added successfully!')
      return redirect('clinics:clinics_list')
    else:
      messages.error(request, 'All fields are required.')

  return render(request, 'clinics/add_clinic.html', {'doctors': doctors})