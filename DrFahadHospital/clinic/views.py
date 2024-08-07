from django.shortcuts import render, get_object_or_404
from .models import Clinic

def clinic_list(request):
    clinics = Clinic.objects.all()
    return render(request, 'clinic/clinic_list.html', {'clinics': clinics})

def clinic_detail(request, clinic_id):
    clinic = get_object_or_404(Clinic, pk=clinic_id)
    return render(request, 'clinic/clinic_detail.html', {'clinic': clinic})
