from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Clinic
from .forms import ClinicForm
from django.core.paginator import Paginator



def clinic_list(request):
    clinics = Clinic.objects.all()

    paginator = Paginator(clinics, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'clinics/clinic_list.html', {'page_obj': page_obj})



def clinic_detail(request, pk):
    clinic = get_object_or_404(Clinic, pk=pk)
    return render(request, 'clinics/clinic_detail.html', {'clinic': clinic})





def is_staff(user):
    return user.is_staff


@user_passes_test(is_staff)
def manage_clinics(request):
    clinics = Clinic.objects.all()

    paginator = Paginator(clinics, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'clinics/manage_clinics.html', {'page_obj': page_obj})



@user_passes_test(is_staff)
def clinic_create(request):
    if request.method == 'POST':
        form = ClinicForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Clinic added successfully.', 'alert-success')
            return redirect('clinics:manage_clinics')
        else:
            messages.error(request, 'Please correct the errors below.', 'alert-danger')
    else:
        form = ClinicForm()
    return render(request, 'clinics/clinic_form.html', {'form': form})



@user_passes_test(is_staff)
def clinic_update(request, pk):
    clinic = get_object_or_404(Clinic, pk=pk)
    if request.method == 'POST':
        form = ClinicForm(request.POST, request.FILES, instance=clinic)
        if form.is_valid():
            form.save()
            messages.success(request, 'Clinic updated successfully.', 'alert-success')
            return redirect('clinics:manage_clinics')
        else:
            messages.error(request, 'Please correct the errors below.', 'alert-danger')
    else:
        form = ClinicForm(instance=clinic)
    return render(request, 'clinics/clinic_form.html', {'form': form})



@user_passes_test(is_staff)
def clinic_delete(request, pk):
    clinic = get_object_or_404(Clinic, pk=pk)
    if request.method == 'POST':
        clinic.delete()
        messages.success(request, 'Clinic deleted successfully.', 'alert-success')
        return redirect('clinics:manage_clinics')
    return render(request, 'clinics/clinic_confirm_delete.html', {'clinic': clinic})
