from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phoneNo = models.CharField(max_length=1024)
    address = models.TextField()
    
    def __str__(self) -> str:
        return f"Profile {self.user.username}"
    

class Bookmark(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # game = models.ForeignKey(Game, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)





