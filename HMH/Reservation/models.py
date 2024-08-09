from django.db import models
from django.contrib.auth.models import User 
from Doctor.models import Doctor
from Clinic.models import Clinic
# Create your models here.




class Reservation(models.Model):
    user=models.ForeignKey(User , on_delete=models.CASCADE)
    clinic = models.ForeignKey(Clinic , on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor , on_delete=models.CASCADE)
    data = models.DateField()
    time_slot= models.TimeField()
    create_at = models.DateTimeField(auto_now_add=True)



