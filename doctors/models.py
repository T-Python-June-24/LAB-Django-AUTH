from django.db import models

class Doctor(models.Model):
    SPECIALIZATION_CHOICES = [
        ('CARDIOLOGY', 'Cardiology'),
        ('DERMATOLOGY', 'Dermatology'),
        ('NEUROLOGY', 'Neurology'),
    ]

    full_name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=50, choices=SPECIALIZATION_CHOICES)
    bio = models.TextField()
    photo = models.ImageField(upload_to='doctors/', null=True, blank=True)

    def __str__(self):
        return self.full_name
