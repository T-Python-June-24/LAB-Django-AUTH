from django.db import models

# Create your models here.

class Doctor(models.Model):

    class SpeChoices(models.IntegerChoices):
        SPE1 = 1, "Dentistry"
        SPE2 = 2, "Cardiology"
        SPE3 = 3, "EMT"
        SPE4 = 4, "Dermatology"
        SPE5 = 5, "Orthopedics"
        SPE6 = 6, "Neurology"
        SPE7 = 7, "Pediatric"


    name = models.CharField(max_length=1024)
    specialization = models.CharField(max_length=1024, choices=SpeChoices.choices)
    bio = models.TextField()
    image = models.ImageField(upload_to="images/", default="images/default.jpg")
    # doctors = models.ManyToManyField(Doctor)


    def __str__(self) -> str:
        return self.name
