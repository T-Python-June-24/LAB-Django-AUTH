# Generated by Django 5.0.7 on 2024-08-05 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("doctors", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="doctor",
            name="profile_picture",
            field=models.ImageField(
                blank=True, null=True, upload_to="doctor_profiles/"
            ),
        ),
    ]
