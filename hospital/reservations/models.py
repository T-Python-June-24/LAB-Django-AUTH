from django.db import models
from doctors.models import Doctor
from clinic.models import Clinic
from django.contrib.auth.models import User

# Create your models here.

class Reservation(models.Model):

    class TimesChoices(models.IntegerChoices):
        TIME1 = 1, "8:00 - 8:30"
        TIME2 = 2, "8:30 - 9:00"
        TIME3 = 3, "9:00 - 9:30"
        TIME4 = 4, "9:30 - 10:00"
        TIME5 = 5, "10:00 - 10:30"
        TIME6 = 6, "10:30 - 11:00"
        TIME7 = 7, "11:00 - 11:30"
        TIME8 = 8, "11:30 - 12:00"
        TIME9 = 9, "12:00 - 12:30"
        TIME10 = 10, "12:30 - 13:00"
        TIME11 = 11, "13:00 - 13:30"
        TIME12 = 12, "13:30 - 14:00"
        TIME13 = 13, "14:00 - 14:30"
        TIME14 = 14, "14:30 - 15:00"
        TIME15 = 15, "15:00 - 15:30"
        TIME16 = 16, "15:30 - 16:00"
        TIME17 = 17, "16:00 - 16:30"
        TIME18 = 18, "16:30 - 17:00"
        TIME19 = 19, "17:00 - 17:30"
        TIME20 = 20, "17:30 - 18:00"

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    date = models.DateField()
    TimeSlot = models.TimeField(choices=TimesChoices.choices)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.user