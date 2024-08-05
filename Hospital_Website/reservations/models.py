from django.db import models
from django.contrib.auth.models import User
from clinics.models import Clinic
from doctors.models import Doctor

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    time_slot = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Reservation by {self.user.username} at {self.clinic.name} with {self.doctor.full_name}'
