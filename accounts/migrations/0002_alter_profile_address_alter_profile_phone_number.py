# Generated by Django 5.0.7 on 2024-08-05 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="address",
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="profile",
            name="phone_number",
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
