# Generated by Django 5.0.7 on 2024-08-08 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('doctors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clinic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024)),
                ('description', models.TextField()),
                ('workingHours', models.CharField(choices=[('08:00-12:00', 'Morning Hours: (08:00-12:00)'), ('12:00-16:00', 'Noon Hours: (12:00-16:00)'), ('16:00-20:00', 'Night Hours: (16:00-20:00)')], max_length=64)),
                ('featureImg', models.ImageField(default='images/default.jpg', upload_to='images/')),
                ('doctors', models.ManyToManyField(to='doctors.doctor')),
            ],
        ),
    ]
