from django.db import models

# Create your models here.


class Doctor(models.Model):
    class Specializations(models.TextChoices):
        PEDIATRICS = "Pediatrics", "Pediatrics"
        INTERNAL_MEDICINE = "Internal Medicine", "Internal Medicine"
        OBSTETRICS_GYNECOLOGY = "Obstetrics and Gynecology", "Obstetrics and Gynecology"
        OPHTHALMOLOGY = "Ophthalmology", "Ophthalmology"
        X_RAY_PLACE = "X_Ray Place", "X-Ray Place"
        BONE_JOINT_SURGERY = "Bone and Joint Surgery", "Bone and Joint Surgery"
        NEUROLOGY = "Neurology", "Neurology"
        GENERAL_SURGERY = "General Surgery", "General Surgery"
    
    
    full_name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255 , choices=Specializations.choices)
    bio = models.TextField()
    photo = models.ImageField(upload_to='images/doctoor/' ,default='images/doctor/default.png')
