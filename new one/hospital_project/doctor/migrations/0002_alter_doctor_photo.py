# Generated by Django 5.1 on 2024-08-10 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='doctor_photos/'),
        ),
    ]
