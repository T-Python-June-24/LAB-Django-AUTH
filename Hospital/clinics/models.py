from django.db import models
from doctors.models import Doctor

# Create your models here.

TIME_SLOTS = [
    ('09:00', '09:00 AM'),
    ('09:30', '09:30 AM'),
    ('10:00', '10:00 AM'),
    ('10:30', '10:30 AM'),
    ('11:00', '11:00 AM'),
    ('11:30', '11:30 AM'),
    ('12:00', '12:00 PM'),
    ('12:30', '12:30 PM'),
    ('13:00', '01:00 PM'),
    ('13:30', '01:30 PM'),
    ('14:00', '02:00 PM'),
    ('14:30', '02:30 PM'),
    ('15:00', '03:00 PM'),
    ('15:30', '03:30 PM'),
    ('16:00', '04:00 PM'),
    ('16:30', '04:30 PM'),
]


class Clinic(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    working_hours = models.CharField(max_length=5, choices=TIME_SLOTS)
    feature_image = models.ImageField(upload_to='images/', default='images/default-clinic.webp')
    doctors = models.ManyToManyField(Doctor, related_name='clinics')

    def __str__(self):
        return self.name
