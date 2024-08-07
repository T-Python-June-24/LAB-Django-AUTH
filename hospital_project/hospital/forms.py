from django import forms
from .models import Profile, Reservation, Clinic, Doctor
from django.contrib.auth.forms import AuthenticationForm

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name','phone_number', 'address']
        widgets = {
            'lab_results': forms.Textarea(attrs={'rows': 4}),
            'other_info': forms.Textarea(attrs={'rows': 4}),
        }
        
class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['doctor', 'date', 'time_slot']

class CustomLoginForm(AuthenticationForm):
    pass

class ClinicForm(forms.ModelForm):
    class Meta:
        model = Clinic
        fields = ['name', 'description', 'working_hours', 'feature_image', 'doctors']

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['full_name', 'specialization', 'bio', 'photo']
        widgets = {
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'clinic': forms.Select(attrs={'class': 'form-control'}),
        }