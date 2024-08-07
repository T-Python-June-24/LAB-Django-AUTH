from django import forms
from .models import Reservation
from doctors.models import Doctor
from clinics.models import Clinic
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['clinic', 'doctor', 'date', 'time_slot']
        widgets = {
            'clinic': forms.Select(attrs={'class': 'select select-bordered w-full'}),
            'doctor': forms.Select(attrs={'class': 'select select-bordered w-full'}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'input input-bordered w-full'}),
            'time_slot': forms.TimeInput(attrs={'type': 'time', 'class': 'input input-bordered w-full'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['doctor'].queryset = Doctor.objects.none()

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'select select-bordered w-full' if isinstance(self.fields[field].widget, forms.Select) else 'input input-bordered w-full'

        if 'clinic' in self.data:
            try:
                clinic_id = int(self.data.get('clinic'))
                self.fields['doctor'].queryset = Doctor.objects.filter(clinics__id=clinic_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['doctor'].queryset = self.instance.clinic.doctors.all()

    def clean(self):
        cleaned_data = super().clean()
        clinic = cleaned_data.get('clinic')
        time_slot = cleaned_data.get('time_slot')

        if clinic and time_slot:
            if time_slot < clinic.opening_time or time_slot > clinic.closing_time:
                raise ValidationError(_("The selected time is outside of the clinic's working hours."))

        return cleaned_data
