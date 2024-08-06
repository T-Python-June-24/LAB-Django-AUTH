from django.db import models
from doctors.models import Doctor
from django.utils import timezone

class Clinic(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    opening_time = models.TimeField(default=timezone.now().replace(hour=9, minute=0, second=0, microsecond=0).time())
    closing_time = models.TimeField(default=timezone.now().replace(hour=17, minute=0, second=0, microsecond=0).time())
    feature_image = models.ImageField(upload_to='clinics/', null=True, blank=True)
    doctors = models.ManyToManyField(Doctor, related_name='clinics')

    def __str__(self):
        return self.name

    @property
    def working_hours(self):
        return f"{self.opening_time.strftime('%H:%M')} - {self.closing_time.strftime('%H:%M')}"
