from django.db import models
from doctor.models import Doctor

class Clinic(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    working_hours = models.CharField(max_length=255)
    feature_image = models.ImageField(upload_to='clinic_images/')
    doctors = models.ManyToManyField(Doctor)

    def __str__(self):
        return self.name
