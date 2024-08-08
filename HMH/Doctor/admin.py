from django.contrib import admin
from .models import Doctor
# Register your models here.

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'specialization') 


admin.site.register(Doctor)