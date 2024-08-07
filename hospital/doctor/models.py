from django.db import models

# Create your models here.
class Doctor(models.Model):

    full_name=models.CharField(max_length=100)
    specilaization=models.CharField(max_length=100)
    bio=models.TextField()
    photo=models.ImageField(upload_to="images/",default="images/default.svg")
    university=models.CharField(max_length=100,default="Student")
    country=models.CharField(max_length=100,default="KSA")
    x_link=models.URLField(null=True)
    instagram_link=models.URLField(null=True)
    facebook_link=models.URLField(null=True)