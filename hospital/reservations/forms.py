from django import forms
from .models import Reservation
from django.core.exceptions import ValidationError
from datetime import datetime

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['clinic', 'doctor', 'date', 'TimeSlot']

    def clean_reservation_date(self):
        date = self.cleaned_data.get('date')
        if date < datetime.now().date():
            raise ValidationError('Reservation date must be in the future.')
        return date

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        TimeSlot = cleaned_data.get('TimeSlot')

        if date and TimeSlot:
            now = datetime.now()
            # Check if the reservation date is today
            if date == now.date():
                # Check if the reservation time is in the past
                if TimeSlot <= now.time():
                    raise ValidationError('You must choose an ahead time. Past is Gone')

        return cleaned_data