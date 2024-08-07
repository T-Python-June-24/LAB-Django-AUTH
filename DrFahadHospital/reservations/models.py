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

    class Meta:
        unique_together = ('doctor', 'date', 'time_slot')

    def __str__(self):
        return f'{self.user.username} - {self.clinic.name} - {self.doctor.full_name} on {self.date} at {self.time_slot}'
