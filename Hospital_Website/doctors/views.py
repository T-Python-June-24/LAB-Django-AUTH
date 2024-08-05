from django.shortcuts import render, redirect
from .models import Doctor
from .forms import DoctorForm

def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctors/doctor_list.html', {'doctors': doctors})

def doctor_detail(request, pk):
    doctor = Doctor.objects.get(pk=pk)
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

def doctor_update(request, pk):
    doctor = Doctor.objects.get(pk=pk)
    if request.method == 'POST':
        form = DoctorForm(request.POST, request.FILES, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('doctors:doctor_list')
    else:
        form = DoctorForm(instance=doctor)
    return render(request, 'doctors/doctor_form.html', {'form': form})

def doctor_delete(request, pk):
    doctor = Doctor.objects.get(pk=pk)
    if request.method == 'POST':
        doctor.delete()
        return redirect('doctors:doctor_list')
    return render(request, 'doctors/doctor_confirm_delete.html', {'doctor': doctor})
