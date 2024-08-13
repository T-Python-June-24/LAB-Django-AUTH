from django.db import models
from django.contrib.auth.models import User
from clinics.models import Clinic
from doctors.models import Doctor

# Create your models here.

class Reservation(models.Model):
    TIME_SLOT_CHOICES = [
        ('8am', '8 AM'),
        ('9am', '9 AM'),
        ('10am', '10 AM'),
        ('11am', '11 AM'),
        ('12pm', '12 PM'),
        ('1pm', '1 PM'),
        ('2pm', '2 PM'),
        ('3pm', '3 PM'),
        ('4pm', '4 PM'),
        ('5pm', '5 PM'),
        ('6pm', '6 PM'),
        ('7pm', '7 PM'),
        ('8pm', '8 PM'),
        ('9pm', '9 PM'),
        ('10pm', '10 PM'),
        ('11pm', '11 PM'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    time_slot = models.CharField(max_length=10, choices=TIME_SLOT_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reservation by {self.user.username} with Dr. {self.doctor.full_name} at {self.clinic.name}"
