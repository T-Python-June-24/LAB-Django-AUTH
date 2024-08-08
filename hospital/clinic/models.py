from django.db import models
from doctors.models import Doctor
from django.contrib.auth.models import User

# Create your models here.


class Clinic(models.Model):

    name = models.CharField(max_length=1024)
    description = models.TextField()
    workingHours = models.CharField(max_length=64)
    featureImg = models.ImageField(upload_to="images/", default="images/default.jpg")
    doctor = models.ManyToManyField(Doctor)


    def __str__(self) -> str:
        return self.name