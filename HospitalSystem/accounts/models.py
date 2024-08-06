from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField(blank=True)
    # avatar = models.ImageField(upload_to="images/avatars/", default="images/avatars/avatar.webp")
    phone_number = models.CharField(max_length=10)


    def __str__(self) -> str:
        return f"Profile {self.user.username}"
    
