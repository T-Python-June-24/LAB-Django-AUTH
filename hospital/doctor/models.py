from django.db import models

# Create your models here.
class Doctor(models.Model):

    full_name=models.CharField(max_length=100)
    specilaization=models.CharField(max_length=100)
    bio=models.TextField()
    photo=models.ImageField(upload_to="images/",default="images/default.svg")
