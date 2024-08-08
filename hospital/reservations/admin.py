from django.contrib import admin
from .models import Reservation

# Register your models here.

class ReservationAdmin(admin.ModelAdmin):

    list_display = ("user", "doctor", "clinic", "date", "TimeSlot", "created_at")
    list_filter = ("user",)

admin.site.register(Reservation, ReservationAdmin)
