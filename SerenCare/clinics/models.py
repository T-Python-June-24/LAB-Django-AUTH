from django.db import models
from doctors.models import Doctor
from accounts.models import User

# Create your models here.


class TimeSlot(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.start_time.strftime('%I:%M %p')} - {self.end_time.strftime('%I:%M %p')}"


class Clinic(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    working_hours = models.ForeignKey(TimeSlot, on_delete=models.CASCADE)
    feature_image = models.ImageField(upload_to= 'images/', default='images/clinic.jpg')
    doctors = models.ManyToManyField(Doctor)

    def __str__(self) -> str:
        return self.name



class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    clinic = models.ForeignKey(Clinic, on_delete= models.CASCADE)
    doctor= models.ForeignKey(Doctor, on_delete= models.CASCADE)
    date= models.DateField()
    time_slot = models.TimeField()
    created_at= models.DateTimeField(auto_now_add= True)

    def __str__(self) -> str:
        return f"Patient: {self.user.first_name} with Dr. {self.doctor.full_name} at {self.clinic.name} clinic"







