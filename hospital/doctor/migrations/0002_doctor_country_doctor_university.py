# Generated by Django 4.2.13 on 2024-08-07 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("doctor", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="doctor",
            name="country",
            field=models.CharField(default="KSA", max_length=100),
        ),
        migrations.AddField(
            model_name="doctor",
            name="university",
            field=models.CharField(default="Student", max_length=100),
        ),
    ]
