from django.db import models
from doctors.models import Doctor
from django.contrib.auth.models import User

# Create your models here.


class Clinic(models.Model):

    WHChoices = (
        ('08:00-12:00', 'Morning Hours: (08:00-12:00)'),
        ('12:00-16:00', 'Noon Hours: (12:00-16:00)'),
        ('16:00-20:00', 'Night Hours: (16:00-20:00)'),
    )

    name = models.CharField(max_length=1024)
    description = models.TextField()
    workingHours = models.CharField(max_length=64, choices=WHChoices)
    featureImg = models.ImageField(upload_to="images/", default="images/default.jpg")
    doctors = models.ManyToManyField(Doctor)


    def __str__(self) -> str:
        return self.name