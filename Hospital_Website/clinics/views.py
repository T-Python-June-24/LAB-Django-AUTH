from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Clinic
from .forms import ClinicForm
from django.core.paginator import Paginator



def clinic_detail(request, pk):
    clinic = get_object_or_404(Clinic, pk=pk)
    return render(request, 'clinics/clinic_detail.html', {'clinic': clinic})

def clinic_list(request):
    clinic_list = Clinic.objects.all()  # Make sure to call .all() to get a QuerySet
    paginator = Paginator(clinic_list, 10)  # Show 10 clinics per page

    page_number = request.GET.get('page')
    clinics = paginator.get_page(page_number)
    return render(request, 'clinics/clinic_list.html', {'clinics': clinics})


def create_clinic(request):
    if request.method == 'POST':
        form = ClinicForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('clinics:clinic_list'))
    else:
        form = ClinicForm()
    
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
        return redirect('clinics:clinic_list')  # Redirect to the list of clinics after deletion
    return render(request, 'clinics/clinic_confirm_delete.html', {'clinic': clinic})
