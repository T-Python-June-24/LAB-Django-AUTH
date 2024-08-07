from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
SPECIALIZATIONS_CHOICES = [
    ('cardiology', 'Cardiology'),
    ('neurology', 'Neurology'),
    ('orthopedics', 'Orthopedics'),
    ('pediatrics', 'Pediatrics'),
    ('general_practice', 'General Practice'),
]

WORKING_HOURS_CHOICES = [
    ('9 AM - 5 PM', '9 AM - 5 PM'),
    ('8 AM - 4 PM', '8 AM - 4 PM'),
    ('10 AM - 6 PM', '10 AM - 6 PM'),
    ('7 AM - 3 PM', '7 AM - 3 PM'),
]

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return f'{self.user.username} Profile'
    
class Doctor(models.Model):
    full_name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100, choices=SPECIALIZATIONS_CHOICES)
    bio = models.TextField()
    photo = models.ImageField(upload_to='doctors/photos/')
    
    def __str__(self):
        return self.full_name
    
class Clinic(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    working_hours = models.CharField(max_length=100, choices=WORKING_HOURS_CHOICES)
    feature_image = models.ImageField(upload_to='clinics/images/')
    doctors = models.ManyToManyField(Doctor)

    def __str__(self):
        return self.name
    
class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    time_slot = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Reservation for {self.user.username} with Dr. {self.doctor.full_name} at {self.clinic.name} on {self.date} at {self.time_slot}'
    