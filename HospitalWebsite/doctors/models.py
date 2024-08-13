from django.db import models

# Create your models here.

class Doctor(models.Model):
    SPECIALIZATION_CHOICES = [
      ('cardiologist', 'Cardiologist'),
      ('neurologist', 'Neurologist'),
      ('dermatologist', 'Dermatologist'),
      ('oncologist', 'Oncologist'),
      ('pediatrician', 'Pediatrician'),
      ('psychiatrist', 'Psychiatrist'),
      ('gynecologist', 'Gynecologist'),
      ('orthopedist', 'Orthopedist'),
      ('urologist', 'Urologist'),
      ('endocrinologist', 'Endocrinologist'),
    ]

    full_name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=50, choices=SPECIALIZATION_CHOICES)
    bio = models.TextField()
    photo = models.ImageField(upload_to='doctor_photos/')

    def __str__(self) -> str:
        return self.full_name
