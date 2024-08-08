from django.shortcuts import render, get_object_or_404, redirect
from doctors.models import Doctor
from clinics.models import Clinic
from .models import Reservation
from .forms import ReservationForm
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from Notifications.utils import send_reservation_email  
from django.utils.timezone import now

@login_required
def reservation_list(request):
    reservations = Reservation.objects.all() 
    paginator = Paginator(reservations, 9)  

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'clinics': Clinic.objects.all(),
        'doctors': Doctor.objects.all(),
        'form': ReservationForm(), 
    }

    return render(request, 'reservations/reservation_list.html', context)

@login_required
def reservation_create(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation_date = form.cleaned_data['reservation_date']
            clinic = form.cleaned_data['clinic']
            doctor = form.cleaned_data['doctor']

            existing_reservation = Reservation.objects.filter(clinic=clinic, doctor=doctor, reservation_date=reservation_date).exists()

            if existing_reservation:
                messages.error(request, 'There is already a reservation for this clinic and doctor at the selected time.')
            else:
                reservation = form.save(commit=False)
                reservation.user = request.user
                reservation.save()

                subject = 'Your Reservation Confirmation'
                html_template = 'Notifications/reservation_email.html' 
                context = {
                    'username': request.user.username,
                    'clinic_name': clinic.name,
                    'reservation_date': reservation_date,
                }
                recipient_list = [request.user.email]

                send_reservation_email(subject, html_template, context, recipient_list)

                messages.success(request, 'Reservation created successfully!')
                return redirect('reservations:reservation_list')
        else:
            messages.error(request, 'There was an error with your submission. Please correct the errors below.')
    else:
        form = ReservationForm()

    context = {
        'clinics': Clinic.objects.all(),
        'doctors': Doctor.objects.all(),
        'form': form,
        'today': now().date(),
    }
    return render(request, 'reservations/add_reservation.html', context)


def reservation_update(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('reservations:reservation_list')
    else:
        form = ReservationForm(instance=reservation)
    
    context = {
        'clinics': Clinic.objects.all(),
        'doctors': Doctor.objects.all(),
        'form': form, 
    }
    return render(request, 'reservations/update_reservation.html', context)


def reservation_delete(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    if request.method == "POST":
        reservation.delete()
        return redirect('reservations:reservation_list')
    return render(request, 'reservations/reservation_confirm_delete.html', {'reservation': reservation})




