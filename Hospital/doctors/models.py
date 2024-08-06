from django.db import models


# Create your models here.
class Doctor(models.Model):
    SPECIALIZATIONS = [
        ('Cardiology', 'Cardiology'),
        ('Neurology', 'Neurology'),
        ('Orthopedics', 'Orthopedics'),
        ('Pediatrics', 'Pediatrics'),
        ('General', 'General')
    ]
    full_name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100, choices=SPECIALIZATIONS)
    bio = models.TextField()
    photo = models.ImageField(upload_to='images/', default='images/default-doctor.jpg')

    def __str__(self):
        return self.full_name
