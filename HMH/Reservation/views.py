from django.shortcuts import render , redirect
from .models import Reservation
from django.http  import HttpRequest
from .forms import ReservationForm
from django.contrib import messages
from Clinic.models import Clinic
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
# Create your views here.

def add_reservation(request: HttpRequest, clinic_name):
    referer = request.META.get('HTTP_REFERER')
    
    if request.method == 'POST':
        clinic = Clinic.objects.get(name=clinic_name)
        form = ReservationForm(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data['data']
            time_slot = form.cleaned_data['time_slot']
            doctor = form.cleaned_data['doctor']
            
            existing_reservation = Reservation.objects.filter(
                clinic=clinic,
                doctor=doctor,
                data=data,
                time_slot=time_slot
            ).exists()
            
            if existing_reservation:
                messages.error(request, 'There is an existing reservation at the same time. Please change the time.')
                return redirect(referer)
            
           
            reservation = form.save(commit=False)
            reservation.clinic = clinic
            reservation.user = request.user
            reservation.save()
            
            messages.success(request, 'Your appointment has been successfully booked.')
            
            page_html = render_to_string('mail/send_reservation.html', {
                'clinic': clinic,
                'date': data,
                'time': time_slot
            })
            
            send_to = request.user.email
            email_message = EmailMessage(
                f"Your appointment has been scheduled with {clinic.name}",
                page_html,
                settings.EMAIL_HOST_USER,
                [send_to]
            )
            email_message.send()
            
            return redirect(referer)
        
        else:
            messages.error(request, f'Error {form.errors}')
            return redirect(referer)
    
    return redirect(referer)

def delete_reservation(request:HttpRequest , id_reservation):
    referer = request.META.get('HTTP_REFERER')
    reservations=Reservation.objects.get(pk = id_reservation)
    reservations.delete()
    messages.success(request , 'Your reservation has been cancelled')
    return redirect(referer)