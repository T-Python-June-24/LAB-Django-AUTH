from django.shortcuts import render, redirect
from django.http import HttpRequest
from doctors.models import Doctor
from django.core.paginator import Paginator
from django.contrib import messages


# Create your views here.

def doctors_list(request: HttpRequest):
  doctor_list = Doctor.objects.all()
  paginator = Paginator(doctor_list, 5) 
  page_number = request.GET.get('page')
  doctors = paginator.get_page(page_number)
  return render(request, 'doctors/doctors_list.html', {'doctors': doctors})


def doctor_detail(request: HttpRequest, doctor_id: int):
  doctor = Doctor.objects.get(pk=doctor_id)
  return render(request, 'doctors/doctor_detail.html', {'doctor': doctor})


def add_doctor(request: HttpRequest):
  if request.method == 'POST':
    full_name = request.POST.get('full_name')
    specialization = request.POST.get('specialization')
    bio = request.POST.get('bio')
    photo = request.FILES.get('photo')

    if full_name and specialization and bio and photo:
      doctor = Doctor(
        full_name=full_name,
        specialization=specialization,
        bio=bio,
        photo=photo
      )
    doctor.save()
    messages.success(request, 'Doctor added successfully!')
    return redirect('doctors:doctors_list')
  else:
    messages.error(request, 'All fields are required.')

  return render(request, 'doctors/add_doctor.html')
