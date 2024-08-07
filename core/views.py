from django.shortcuts import render
from clinics.models import Clinic
from doctors.models import Doctor
from reservations.models import Reservation
from django.contrib.auth.decorators import user_passes_test
from django.db.models import Q

def home(request):
    clinics = Clinic.objects.all()[:3]
    doctors = Doctor.objects.all()[:3]
    return render(request, 'core/home.html', {'clinics': clinics, 'doctors': doctors})

@user_passes_test(lambda u: u.is_staff)
def staff_dashboard(request):
    recent_reservations = Reservation.objects.order_by('-created_at')[:10]  
    return render(request, 'core/staff_dashboard.html', {'recent_reservations': recent_reservations})

def search(request):
    query = request.GET.get('q')
    search_type = request.GET.get('type', 'all')

    doctors = Doctor.objects.none()
    clinics = Clinic.objects.none()

    if query:
        if search_type in ['all', 'doctors']:
            doctors = Doctor.objects.filter(
                Q(full_name__icontains=query) |
                Q(specialization__icontains=query)
            )

        if search_type in ['all', 'clinics']:
            clinics = Clinic.objects.filter(
                Q(name__icontains=query) |
                Q(description__icontains=query)
            )

    context = {
        'doctors': doctors,
        'clinics': clinics,
        'query': query,
        'search_type': search_type,
    }

    return render(request, 'core/search_results.html', context)
