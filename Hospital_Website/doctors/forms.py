from django import forms
from .models import Doctor

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = "__all__"

class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False, label='Search')
