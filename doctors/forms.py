from django import forms
from .models import Doctor

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['full_name', 'specialization', 'bio', 'photo']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'input input-bordered w-full'}),
            'specialization': forms.Select(attrs={'class': 'select select-bordered w-full'}),
            'bio': forms.Textarea(attrs={'class': 'textarea textarea-bordered w-full', 'rows': 4}),
            'photo': forms.ClearableFileInput(attrs={'class': 'file-input file-input-bordered w-full'}),
        }
