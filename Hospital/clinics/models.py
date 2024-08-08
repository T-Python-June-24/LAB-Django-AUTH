from django.db import models
from doctors.models import Doctor

# Create your models here.

WORKING_HOURS = [
    ('07:00-15:00', 'Morning (07:00-15:00)'),
    ('15:00-23:00', 'Evening (15:00-23:00)'),
]


class Clinic(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    working_hours = models.CharField(max_length=11, choices=WORKING_HOURS)
    feature_image = models.ImageField(upload_to='images/', default='images/default-clinic.webp')
    doctors = models.ManyToManyField(Doctor, related_name='clinics')

    def __str__(self):
        return self.name
