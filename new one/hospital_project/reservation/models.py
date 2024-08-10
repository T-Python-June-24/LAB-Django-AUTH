from django.db import models
from django.contrib.auth import get_user_model
from clinic.models import Clinic
from doctor.models import Doctor

User = get_user_model()

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    time_slot = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reservation for {self.user.username} at {self.clinic.name} on {self.date} at {self.time_slot}"