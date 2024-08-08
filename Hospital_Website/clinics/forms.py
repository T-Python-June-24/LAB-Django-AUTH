from django import forms
from .models import Clinic
from doctors.models import Doctor

class ClinicForm(forms.ModelForm):
    class Meta:
        model = Clinic
        fields = ['name', 'description', 'opening_time', 'closing_time', 'feature_image', 'doctors']
    
    opening_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    closing_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    doctors = forms.ModelMultipleChoiceField(queryset=Doctor.objects.all(), widget=forms.SelectMultiple)
