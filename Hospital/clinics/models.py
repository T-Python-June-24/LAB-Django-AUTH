from django.db import models
from doctors.models import Doctor

class Clinic(models.Model):
    WORKING_HOURS_CHOICES = (
        ('08:00-12:00', 'Morning Shift (08:00-12:00)'),
        ('12:00-16:00', 'Afternoon Shift (12:00-16:00)'),
        ('16:00-20:00', 'Evening Shift (16:00-20:00)'),
    )

    name = models.CharField(max_length=255)
    description = models.TextField()
    working_hours = models.CharField(max_length=11, choices=WORKING_HOURS_CHOICES)
    feature_image = models.ImageField(upload_to='images/', default="images/default.jpg")
    doctors = models.ManyToManyField(Doctor)

    def __str__(self):
        return self.name