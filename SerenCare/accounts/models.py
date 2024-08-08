from django.db import models
from django.contrib.auth.models import User
#from games.models import Game


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True, null= True)
    address = models.TextField(blank=True, null=True)


    def __str__(self) -> str:
        return f"Profile {self.user.username}"
    



# class Bookmark(models.Model):

#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     game = models.ForeignKey(Game, on_delete=models.CASCADE)

#     created_at = models.DateTimeField(auto_now_add=True)





