
from django import forms
from .models import  Reservation
from clinic.models import Clinic

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['clinic', 'doctor', 'date', 'time_slot']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time_slot': forms.Select(choices=[]),
        }