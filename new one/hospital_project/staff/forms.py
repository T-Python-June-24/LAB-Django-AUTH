from django import forms
from clinic.models import Clinic
from doctor.models import Doctor

class ClinicForm(forms.ModelForm):
    class Meta:
        model = Clinic
        fields = ['name', 'description', 'working_hours', 'feature_image', 'doctors']

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['full_name', 'specialization', 'bio', 'photo']