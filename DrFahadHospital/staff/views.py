from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from clinics.models import Clinic
from doctors.models import Doctor

@user_passes_test(lambda u: u.is_staff)
def staff_dashboard(request):
    clinics = Clinic.objects.all()
    doctors = Doctor.objects.all()
    return render(request, 'staff/staff_dashboard.html', {'clinics': clinics, 'doctors': doctors})
