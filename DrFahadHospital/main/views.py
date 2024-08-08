# main/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

from django.db.models import Q
from django.shortcuts import render
from doctor.models import Doctor
from clinic.models import Clinic

def search_results(request):
    query = request.GET.get('q')
    if query:
        clinics = Clinic.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        doctors = Doctor.objects.filter(Q(full_name__icontains=query) | Q(specialization__icontains=query))
    else:
        clinics = Clinic.objects.none()
        doctors = Doctor.objects.none()

    context = {
        'clinics': clinics,
        'doctors': doctors,
        'query': query,
    }
    return render(request, 'search_results.html', context)
