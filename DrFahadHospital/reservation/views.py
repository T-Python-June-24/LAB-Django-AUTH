from django.shortcuts import render, redirect, get_object_or_404
from .models import Reservation
from django.core.exceptions import ValidationError
from .forms import ReservationForm

def reservation_list(request):
    reservations = Reservation.objects.filter(user=request.user)
    return render(request, 'reservation/reservation_list.html', {'reservations': reservations})

def reservation_detail(request, reservation_id):
    reservation = get_object_or_404(Reservation, pk=reservation_id)
    return render(request, 'reservation/reservation_detail.html', {'reservation': reservation})

def reservation_create(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            doctor = form.cleaned_data['doctor']
            clinic = form.cleaned_data['clinic']
            date = form.cleaned_data['date']
            time_slot = form.cleaned_data['time_slot']

            # Check for existing reservations
            if Reservation.objects.filter(doctor=doctor, date=date, time_slot=time_slot).exists():
                form.add_error(None, 'This time slot is already booked. Please choose another time.')
            else:
                form.save()
                # Redirect to reservation list or detail
                return redirect('reservation_list')
    else:
        form = ReservationForm()
    return render(request, 'reservation/reservation_form.html', {'form': form})

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def send_reservation_email(reservation):
    subject = 'Your Reservation Confirmation'
    html_message = render_to_string('reservation_email.html', {'reservation': reservation})
    plain_message = strip_tags(html_message)
    from_email = 'BlueHuawei67_@outlook.com'
    to = reservation.user.email

    send_mail(subject, plain_message, from_email, [to], html_message=html_message)

