
from django.db import models
from doctors.models import Doctor

class Clinic(models.Model):
    WORKING_HOURS_CHOICES = [
    ('09:00 - 12:00', '09:00 - 12:00'),
    ('12:00 - 15:00', '12:00 - 15:00'),
    ('15:00 - 18:00', '15:00 - 18:00'),
    ('18:00 - 21:00', '18:00 - 21:00'),
    ('21:00 - 00:00', '21:00 - 00:00'),
    ('00:00 - 03:00', '00:00 - 03:00'),
    ('03:00 - 06:00', '03:00 - 06:00'),
    ('06:00 - 09:00', '06:00 - 09:00'),
    ('10:00 - 13:00', '10:00 - 13:00'),
    ('13:00 - 16:00', '13:00 - 16:00'),
    ('16:00 - 19:00', '16:00 - 19:00'),
    ('19:00 - 22:00', '19:00 - 22:00'),
]


    name = models.CharField(max_length=255)
    description = models.TextField()
    working_hours = models.CharField(max_length=50, choices=WORKING_HOURS_CHOICES)
    feature_image = models.ImageField(upload_to='clinic_images/')
    doctors = models.ManyToManyField(Doctor, related_name='clinics')

    def __str__(self):
        return self.name
