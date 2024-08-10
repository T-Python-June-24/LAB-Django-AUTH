# reservation/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Reservation
from .forms import ReservationForm
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from clinic.models import Clinic
from doctor.models import Doctor

@login_required
def reservation_list(request):
    reservations = Reservation.objects.filter(user=request.user)
    return render(request, 'reservation/reservation_list.html', {'reservations': reservations})

@login_required
def reservation_detail(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk, user=request.user)
    return render(request, 'reservation/reservation_detail.html', {'reservation': reservation})

login_required
def reservation_cancel(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk, user=request.user)
    if request.method == 'POST':
        reservation.delete()
        return redirect('reservation_list')
    return render(request, 'reservation/reservation_cancel.html', {'reservation': reservation})

@login_required
def create_reservation(request):
    clinic_id = request.GET.get('clinic')
    doctor_id = request.GET.get('doctor')
    initial_data = {}

    if clinic_id:
        clinic = get_object_or_404(Clinic, pk=clinic_id)
        initial_data['clinic'] = clinic

    if doctor_id:
        doctor = get_object_or_404(Doctor, pk=doctor_id)
        initial_data['doctor'] = doctor

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            return redirect('reservation_list')
    else:
        form = ReservationForm(initial=initial_data)

    return render(request, 'reservation/create_reservation.html', {'form': form})

   

def get_doctors_for_clinic(request, clinic_id):
    clinic = get_object_or_404(Clinic, id=clinic_id)
    doctors = clinic.doctors.all().values('id', 'full_name')
    return JsonResponse({'doctors': list(doctors)})








from django.http import JsonResponse
from django.views.decorators.http import require_GET
from .models import Clinic

@require_GET
def get_working_hours_for_clinic(request, clinic_id):
    clinic = Clinic.objects.get(pk=clinic_id)
    return JsonResponse({'working_hours': clinic.working_hours})