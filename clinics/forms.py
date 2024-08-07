from django import forms
from .models import Clinic

class ClinicForm(forms.ModelForm):
    class Meta:
        model = Clinic
        fields = ['name', 'description', 'opening_time', 'closing_time', 'feature_image', 'doctors']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input input-bordered w-full'}),
            'description': forms.Textarea(attrs={'class': 'textarea textarea-bordered w-full', 'rows': 4}),
            'opening_time': forms.TimeInput(attrs={'type': 'time', 'class': 'input input-bordered w-full'}),
            'closing_time': forms.TimeInput(attrs={'type': 'time', 'class': 'input input-bordered w-full'}),
            'feature_image': forms.ClearableFileInput(attrs={'class': 'file-input file-input-bordered w-full'}),
            'doctors': forms.SelectMultiple(attrs={'class': 'select select-bordered w-full'}),
        }
