from django.shortcuts import render
from clinics.models import Clinic
from doctors.models import Doctor
from reservations.models import Reservation
from django.contrib.auth.models import User



def home(request):
    # Statistics
    total_clinics = Clinic.objects.count()
    total_doctors = Doctor.objects.count()
    total_reservations = Reservation.objects.count()
    total_users = User.objects.count()

    # Data for charts (example data)
    clinics = Clinic.objects.all()
    clinic_names = [clinic.name for clinic in clinics]
    clinic_reservations = [clinic.reservation_set.count() for clinic in clinics]

    context = {
        'total_clinics': total_clinics,
        'total_doctors': total_doctors,
        'total_reservations': total_reservations,
        'total_users': total_users,
        'clinic_names': clinic_names,
        'clinic_reservations': clinic_reservations,
    }
    return render(request, 'main/home.html', context)
