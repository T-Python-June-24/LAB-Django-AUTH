from django.db import models

# Create your models here.

class Doctor(models.Model):
   
    class Specialization(models.TextChoices):
        
       SPE1 = "DENT", "Dentistry"
       SPE2 = "CARD", "Cardiology"
       SPE3 = "EMT", "EMT"
       SPE4 = "DERM", "Dermatology"
       SPE5 = "ORTH", "Orthopedics"
       SPE6 = "NEUR", "Neurology"
       SPE7 = "PEDI", "Pediatric"

    
    full_name = models.CharField(max_length=1024)
    specialization = models.CharField(max_length=64, choices=Specialization.choices, default=Specialization)
    bio = models.TextField()
    photo = models.ImageField(upload_to='images/', default="images/default.jpg")

    def __str__(self):
        return f"{self.full_name} - {self.specialization}"
