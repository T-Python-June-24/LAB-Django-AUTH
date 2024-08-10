from django.db import models

class Doctor(models.Model):
    full_name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    bio = models.TextField()
    photo = models.ImageField(upload_to='doctor_photos/', blank=True, null=True)

    def __str__(self):
        return self.full_name