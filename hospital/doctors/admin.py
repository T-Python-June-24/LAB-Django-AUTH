from django.contrib import admin
from .models import Doctor

# Register your models here.

class DoctorAdmin(admin.ModelAdmin):

    list_display = ("name", "specialization", "bio", "image",)
    list_filter = ("name",)

admin.site.register(Doctor, DoctorAdmin)

