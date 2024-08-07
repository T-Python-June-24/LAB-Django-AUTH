from django.db import models

class Doctor(models.Model):
    full_name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)
    bio = models.TextField()
    photo = models.ImageField(upload_to='doctor_images/')

    def __str__(self):
        return self.full_name
