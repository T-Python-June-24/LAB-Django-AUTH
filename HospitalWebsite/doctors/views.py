from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Doctor
from .forms import DoctorForm
from django.core.paginator import Paginator



def doctor_list(request):
    doctors = Doctor.objects.all()

    paginator = Paginator(doctors, 10) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'doctors/doctor_list.html', {'page_obj': page_obj})

def doctor_detail(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    return render(request, 'doctors/doctor_detail.html', {'doctor': doctor})







def is_staff(user):
    return user.is_staff


@user_passes_test(is_staff)
def manage_doctors(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctors/manage_doctors.html', {'doctors': doctors})



@user_passes_test(is_staff)
def doctor_create(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Doctor added successfully.', 'alert-success')
            return redirect('doctors:manage_doctors')
    else:
        form = DoctorForm()
    return render(request, 'doctors/doctor_form.html', {'form': form})



@user_passes_test(is_staff)
def doctor_update(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        form = DoctorForm(request.POST, request.FILES, instance=doctor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Doctor updated successfully.', 'alert-success')
            return redirect('doctors:manage_doctors')
    else:
        form = DoctorForm(instance=doctor)
    return render(request, 'doctors/doctor_form.html', {'form': form})



@user_passes_test(is_staff)
def doctor_delete(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        doctor.delete()
        messages.success(request, 'Doctor deleted successfully.', 'alert-success')
        return redirect('doctors:manage_doctors')
    return render(request, 'doctors/doctor_confirm_delete.html', {'doctor': doctor})
