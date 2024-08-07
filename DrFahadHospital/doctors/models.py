from django.db import models

class Doctor(models.Model):
    SPECIALIZATIONS = [
        ('Cardiology', 'Cardiology'),
        ('Neurology', 'Neurology'),
        ('Orthopedics', 'Orthopedics'),
        # Add more specializations as needed
    ]
    full_name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255, choices=SPECIALIZATIONS)
    bio = models.TextField()
    photo = models.ImageField(upload_to='doctor_photos/')

    def __str__(self):
        return self.full_name
