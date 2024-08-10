from django.db import models
from doctor.models import Doctor

class Clinic(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    working_hours = models.CharField(max_length=255, choices=[
        
        ('09:00-17:00', '9:00 AM - 5:00 PM'),
        ('10:00-18:00', '10:00 AM - 6:00 PM'),
        ('11:00-19:00', '11:00 AM - 7:00 PM'),
        # Add more choices as needed
    ])
    feature_image = models.ImageField(upload_to='clinic_images/', blank=True, null=True)
    doctors = models.ManyToManyField(Doctor, related_name='clinics')

    def __str__(self):
        return self.name