from django.db import models
from doctors.models import Doctor

# Create your models here.

class Clinic(models.Model):
    WORKING_HOURS_CHOICES = [
        ('8am-4pm', '8 AM - 4 PM'),
        ('4pm-11pm', '4 AM - 11 PM'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    working_hours = models.CharField(max_length=20, choices=WORKING_HOURS_CHOICES)
    feature_image = models.ImageField(upload_to='clinic_images/')
    doctors = models.ManyToManyField(Doctor)

    def __str__(self) -> str:
        return self.name
