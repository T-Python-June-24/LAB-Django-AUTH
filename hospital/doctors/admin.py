from django.contrib import admin
from .models import Doctor

# Register your models here.

class DoctorAdmin(admin.ModelAdmin):

    list_display = ("full_name", "specialization", "bio", "photo",)
    list_filter = ("full_name",)

admin.site.register(Doctor, DoctorAdmin)

