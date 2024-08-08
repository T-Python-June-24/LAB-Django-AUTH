# Generated by Django 5.0.7 on 2024-08-06 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='specialization',
            field=models.CharField(choices=[('CARD', 'Cardiology'), ('DERM', 'Dermatology'), ('NEUR', 'Neurology'), ('ORTH', 'Orthopedics'), ('PEDI', 'Pediatrics'), ('GAST', 'Gastroenterology'), ('OBGY', 'Obstetrics and Gynecology'), ('ENDO', 'Endocrinology'), ('ONCO', 'Oncology'), ('UROL', 'Urology'), ('OPHT', 'Ophthalmology')], default='ENDO', max_length=64),
        ),
    ]
