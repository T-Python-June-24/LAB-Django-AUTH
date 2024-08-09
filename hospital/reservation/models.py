from django.db import models
from django.contrib.auth.models import User
from doctor.models import Doctor
from clinic.models import Clinic

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    time_slot = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reservation for {self.user.username} on {self.date} at {self.time_slot} with Dr. {self.doctor.full_name}"
