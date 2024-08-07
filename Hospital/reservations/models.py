from django.db import models
from profiles.models import Profile
from clinics.models import Clinic
from doctors.models import Doctor
# Create your models here.

class Reservation(models.Model):
    user=models.ForeignKey(Profile,on_delete=models.CASCADE)
    clinic=models.ForeignKey(Clinic,on_delete=models.CASCADE)
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    date = models.DateField()
    time_slot = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.user.username} - {self.date} at {self.time_slot}"