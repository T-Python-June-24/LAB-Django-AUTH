from django.db import models

class Doctor(models.Model):
    SPECIALIZATIONS = (
   ('CARD', 'Cardiology'),
    ('DERM', 'Dermatology'),
    ('NEUR', 'Neurology'),
    ('ORTH', 'Orthopedics'),
    ('PEDI', 'Pediatrics'),
    ('GAST', 'Gastroenterology'),
    ('OBGY', 'Obstetrics and Gynecology'),
    ('ONCO', 'Oncology'),
    ('PSYC', 'Psychiatry'),
    ('ENDO', 'Endocrinology'),
    ('UROL', 'Urology'),
    ('OPHT', 'Ophthalmology'),
    )

    full_name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=4, choices=SPECIALIZATIONS)
    bio = models.TextField()
    photo = models.ImageField(upload_to='images/', default="images/default.jpg")

    def __str__(self):
        return f"{self.full_name} - {self.specialization}"