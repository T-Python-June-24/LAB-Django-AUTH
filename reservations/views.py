from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Reservation
from .forms import ReservationForm
from django.contrib import messages
from django.db.models import Q
from clinics.models import Clinic
from doctors.models import Doctor
from datetime import timedelta
from django.utils import timezone

@login_required
def reservation_list(request):
    reservations = Reservation.objects.filter(user=request.user)
    messages.info(request, f"You have {reservations.count()} reservation(s).")
    return render(request, 'reservations/reservation_list.html', {'reservations': reservations})

@login_required
def create_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            new_reservation = form.save(commit=False)

            # Check for conflicting reservations
            conflicting_reservations = Reservation.objects.filter(
                doctor=new_reservation.doctor,
                date=new_reservation.date,
                time__range=(
                    new_reservation.time - timedelta(hours=1),
                    new_reservation.time + timedelta(hours=1)
                )
            )

            if conflicting_reservations.exists():
                messages.error(request, "There is already a reservation within 1 hour of this time for this doctor.")
                return render(request, 'reservations/create_reservation.html', {'form': form})

            new_reservation.user = request.user
            new_reservation.save()
            messages.success(request, 'Reservation created successfully.')
            return redirect('reservation_list')
    else:
        form = ReservationForm()

    clinics = Clinic.objects.all()
    doctors = Doctor.objects.all()
    return render(request, 'reservations/create_reservation.html', {
        'form': form,
        'clinics': clinics,
        'doctors': doctors
    })

@login_required
def reservation_detail(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk, user=request.user)
    messages.info(request, f"Viewing details for reservation on {reservation.date}")
    return render(request, 'reservations/reservation_detail.html', {'reservation': reservation})

@login_required
def cancel_reservation(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk, user=request.user)
    if request.method == 'POST':
        reservation.delete()
        messages.success(request, "Reservation cancelled successfully.")
        return redirect('reservation_list')
    messages.warning(request, "Are you sure you want to cancel this reservation?")
    return render(request, 'reservations/cancel_reservation.html', {'reservation': reservation})
@login_required
def get_doctors(request, clinic_id):
    doctors = Doctor.objects.filter(clinics__id=clinic_id).values('id', 'full_name')
    return JsonResponse(list(doctors), safe=False)
