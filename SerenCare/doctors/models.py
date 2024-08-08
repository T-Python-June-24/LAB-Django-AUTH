from django.db import models

# Create your models here.

class Doctor(models.Model):
    full_name = models.CharField(max_length=128)
    specialization = models.CharField(max_length=128)
    bio = models.TextField()
    photo = models.ImageField(upload_to= 'images/avatars/', default='images/avtars/avatar.png')

    def __str__(self) -> str:
        return f"Dr. {self.full_name}"
