from django.db import models
from doctors.models import Doctor

# Create your models here.

class Clinic(models.Model):
    WORKING_HOURS_CHOICES = [
        ('9am-5pm', '9 AM - 5 PM'),
        ('10am-6pm', '10 AM - 6 PM'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    working_hours = models.CharField(max_length=20, choices=WORKING_HOURS_CHOICES)
    feature_image = models.ImageField(upload_to='clinic_images/')
    doctors = models.ManyToManyField(Doctor)

    def __str__(self) -> str:
        return self.name
