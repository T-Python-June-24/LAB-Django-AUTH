from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import ReservationForm
from .models import Reservation



@login_required
def make_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            messages.success(request, 'Reservation made successfully.', 'alert-success')
            return redirect('reservations:user_reservations')
    else:
        form = ReservationForm()
    return render(request, 'reservations/make_reservation.html', {'form': form})




@login_required
def user_reservations(request):
    reservations = Reservation.objects.filter(user=request.user)
    return render(request, 'reservations/user_reservations.html', {'reservations': reservations})




@login_required
def cancel_reservation(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk, user=request.user)
    if request.method == 'POST':
        reservation.delete()
        messages.success(request, 'Reservation cancelled successfully.', 'alert-success')
        return redirect('reservations:user_reservations')
    return render(request, 'reservations/cancel_reservation.html', {'reservation': reservation})
