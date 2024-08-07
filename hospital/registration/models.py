from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone_number=models.CharField(max_length=10)
    address=models.TextField()
    image=models.ImageField(upload_to="images/",default="images/default.svg")