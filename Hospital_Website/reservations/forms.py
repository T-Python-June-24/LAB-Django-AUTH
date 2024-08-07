from django import forms
from .models import Reservation
from django.core.exceptions import ValidationError
from datetime import datetime

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['clinic', 'doctor', 'reservation_date', 'reservation_time']

    def clean_reservation_date(self):
        reservation_date = self.cleaned_data.get('reservation_date')
        if reservation_date < datetime.now().date():
            raise ValidationError('Reservation date must be in the future.')
        return reservation_date

    def clean(self):
        cleaned_data = super().clean()
        reservation_date = cleaned_data.get('reservation_date')
        reservation_time = cleaned_data.get('reservation_time')

        if reservation_date and reservation_time:
            now = datetime.now()
            # Check if the reservation date is today
            if reservation_date == now.date():
                # Check if the reservation time is in the past
                if reservation_time <= now.time():
                    raise ValidationError('Reservation time must be in the future.')

        return cleaned_data
