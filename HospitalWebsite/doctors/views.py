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


def update_doctor(request: HttpRequest, doctor_id: int):
    if not request.user.is_authenticated or not request.user.is_staff:
        messages.error(request, 'You do not have permission to access this page.')
        return redirect('doctors:doctors_list')

    try:
        doctor = Doctor.objects.get(pk=doctor_id)
    except Doctor.DoesNotExist:
        messages.error(request, 'Doctor not found.')
        return redirect('doctors:doctors_list')

    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        specialization = request.POST.get('specialization')
        bio = request.POST.get('bio')
        photo = request.FILES.get('photo')

        if full_name and specialization and bio:
            doctor.full_name = full_name
            doctor.specialization = specialization
            doctor.bio = bio
            if photo:
                doctor.photo = photo
            doctor.save()
            messages.success(request, 'Doctor updated successfully!')
            return redirect('doctors:doctors_list')
        else:
            messages.error(request, 'All fields are required.')

    return render(request, 'doctors/update_doctor.html', {'doctor': doctor})


def delete_doctor(request: HttpRequest, doctor_id: int):
    if not request.user.is_authenticated or not request.user.is_staff:
        messages.error(request, 'You do not have permission to access this page.')
        return redirect('doctors:doctors_list')

    try:
        doctor = Doctor.objects.get(pk=doctor_id)
    except Doctor.DoesNotExist:
        messages.error(request, 'Doctor not found.')
        return redirect('doctors:doctors_list')

    if request.method == 'POST':
        doctor.delete()
        messages.success(request, 'Doctor deleted successfully!')
        return redirect('doctors:doctors_list')

    return render(request, 'doctors/delete_doctor.html', {'doctor': doctor})