from django.db import models

class Doctor(models.Model):
   
    class Specialization(models.TextChoices):
        CARD = "CARD", "Cardiology"
        DERM = "DERM",  "Dermatology"
        NEUR = "NEUR", "Neurology"
        ORTH = "ORTH", "Orthopedics"
        PEDI = "PEDI", "Pediatrics"
        GAST = "GAST", "Gastroenterology"
        OBGY="OBGY","Obstetrics and Gynecology"
        ENDO="ENDO","Endocrinology"
        ONCO="ONCO","Oncology"
        UROL="UROL","Urology"
        OPHT="OPHT","Ophthalmology"

    


    full_name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=64, choices=Specialization.choices, default=Specialization.ENDO)
    bio = models.TextField()
    photo = models.ImageField(upload_to='images/', default="images/default.jpg")

    def __str__(self):
        return f"{self.full_name} - {self.specialization}"