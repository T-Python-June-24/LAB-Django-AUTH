from django.db import models


# Create your models here.
class Doctor(models.Model):
    class Specialization(models.TextChoices):
        CARDIOLOGY = ('Cardiology', 'Cardiology')
        NEUROLOGY = ('Neurology', 'Neurology')
        ORTHOPEDICS = ('Orthopedics', 'Orthopedics')
        PEDIATRICS = ('Pediatrics', 'Pediatrics')
        GENERAL = ('General', 'General')

    full_name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100, choices=Specialization.choices)
    bio = models.TextField()
    photo = models.ImageField(upload_to='images/', default='images/default-doctor.jpg')

    def __str__(self):
        return self.full_name
