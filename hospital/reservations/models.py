from django.db import models
from doctors.models import Doctor
from clinics.models import Clinic
from django.contrib.auth.models import User

# Create your models here.

class Reservation(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    date = models.DateField()
    TimeSlot = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return f"Reservation for {self.user.username} with {self.doctor.full_name} at {self.clinic.name}"