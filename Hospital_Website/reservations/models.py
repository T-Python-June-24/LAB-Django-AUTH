from django.db import models
from django.contrib.auth.models import User
from clinics.models import Clinic
from doctors.models import Doctor

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    reservation_date = models.DateField()
    reservation_time = models.TimeField()

    def __str__(self):
        return f"Reservation for {self.user.username} with {self.doctor.full_name} at {self.clinic.name}"
