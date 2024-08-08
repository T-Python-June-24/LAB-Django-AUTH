from django.contrib import admin
from clinics.models import Clinic,TimeSlot,Reservation

# Register your models here.
admin.site.register(Clinic)
admin.site.register(TimeSlot)
admin.site.register(Reservation)