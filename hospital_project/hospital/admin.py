from django.contrib import admin
from .models import Clinic, Doctor

# Register your models here.

admin.site.register(Clinic)
admin.site.register(Doctor)