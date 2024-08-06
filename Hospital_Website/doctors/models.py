from django.db import models


class Doctor(models.Model):
    SPECIALIZATIONS = [
    ('Cardiology', 'Cardiology'),
    ('Dermatology', 'Dermatology'),
    ('Neurology', 'Neurology'), 
    ('Oncology', 'Oncology'),
    ('Pediatrics', 'Pediatrics'),
    ('Psychiatry', 'Psychiatry'),
    ('Radiology', 'Radiology'),
    ('Surgery', 'Surgery'),
    ('Orthopedics', 'Orthopedics'),
    ('Internal Medicine', 'Internal Medicine'),
    ('Gastroenterology', 'Gastroenterology'),
    ('Endocrinology', 'Endocrinology'),
    ('Rheumatology', 'Rheumatology'),
    ('Urology', 'Urology'),
    ('Pulmonology', 'Pulmonology'),
    ('Hematology', 'Hematology'),
    ('Nephrology', 'Nephrology'),
    ('Infectious Diseases', 'Infectious Diseases'),
    ('Allergy and Immunology', 'Allergy and Immunology'),
    ('Geriatrics', 'Geriatrics'),
    ('Obstetrics and Gynecology', 'Obstetrics and Gynecology'),
]

    full_name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=50, choices=SPECIALIZATIONS)
    bio = models.TextField()
    photo = models.ImageField(upload_to='doctor_photos/')

    def __str__(self):
        return self.full_name
