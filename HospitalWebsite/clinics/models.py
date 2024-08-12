from django.db import models
from doctors.models import Doctor



class Clinic(models.Model):
    WORKING_HOURS = [
        ('08:00-12:00', '08:00-12:00'),
        ('12:00-16:00', '12:00-16:00'),
        ('16:00-20:00', '16:00-20:00'),
        # Add other time slots here
    ]
    name = models.CharField(max_length=255)
    description = models.TextField()
    working_hours = models.CharField(max_length=20, choices=WORKING_HOURS)
    feature_image = models.ImageField(upload_to='clinic_images/')
    doctors = models.ManyToManyField(Doctor)

    def __str__(self):
        return self.name
