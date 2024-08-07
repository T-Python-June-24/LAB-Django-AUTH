from django import forms
from .models import Profile, Reservation
from django.contrib.auth.forms import AuthenticationForm

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone_number', 'address']

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['doctor', 'date', 'time_slot']

class CustomLoginForm(AuthenticationForm):
    pass