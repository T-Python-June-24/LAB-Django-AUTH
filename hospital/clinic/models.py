from django.db import models
from doctor.models import Doctor

class Clinic(models.Model):
    class WorkingHours(models.TextChoices):
        MON_FRI_8AM_6PM = 'MON_FRI_8AM_6PM', 'Monday - Friday: 8:00 AM - 6:00 PM'
        MON_FRI_9AM_5PM_SAT_9AM_1PM = 'MON_FRI_9AM_5PM_SAT_9AM_1PM', 'Monday - Friday: 9:00 AM - 5:00 PM, Saturday: 9:00 AM - 1:00 PM'
        MON_WED_8AM_5PM_THURS_9AM_6PM_FRI_8AM_3PM = 'MON_WED_8AM_5PM_THURS_9AM_6PM_FRI_8AM_3PM', 'Monday - Wednesday: 8:00 AM - 5:00 PM, Thursday: 9:00 AM - 6:00 PM, Friday: 8:00 AM - 3:00 PM'
        MON_FRI_9AM_5PM_SAT_10AM_3PM = 'MON_FRI_9AM_5PM_SAT_10AM_3PM', 'Monday - Friday: 9:00 AM - 5:00 PM, Saturday: 10:00 AM - 3:00 PM'
        MON_FRI_8AM_5PM_SAT_9AM_2PM = 'MON_FRI_8AM_5PM_SAT_9AM_2PM', 'Monday - Friday: 8:00 AM - 5:00 PM, Saturday: 9:00 AM - 2:00 PM'
        MON_THURS_8AM_7PM_FRI_8AM_5PM_SAT_9AM_1PM = 'MON_THURS_8AM_7PM_FRI_8AM_5PM_SAT_9AM_1PM', 'Monday - Thursday: 8:00 AM - 7:00 PM, Friday: 8:00 AM - 5:00 PM, Saturday: 9:00 AM - 1:00 PM'
        MON_FRI_9AM_6PM_SAT_10AM_2PM = 'MON_FRI_9AM_6PM_SAT_10AM_2PM', 'Monday - Friday: 9:00 AM - 6:00 PM, Saturday: 10:00 AM - 2:00 PM'
        MON_FRI_7AM_6PM_SAT_8AM_1PM = 'MON_FRI_7AM_6PM_SAT_8AM_1PM', 'Monday - Friday: 7:00 AM - 6:00 PM, Saturday: 8:00 AM - 1:00 PM'
        DAILY_8AM_8PM = 'DAILY_8AM_8PM', 'Monday - Sunday: 8:00 AM - 8:00 PM'

    name = models.CharField(max_length=100)
    description = models.TextField()
    working_hours = models.CharField(
        max_length=1024,
        choices=WorkingHours.choices,
        default=WorkingHours.MON_FRI_8AM_6PM
    )
    doctor = models.ManyToManyField(Doctor)
