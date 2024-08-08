from django.contrib import admin
from clinic.models import Clinic
from reservation.models import Reservation


admin.site.register(Clinic)
admin.site.register(Reservation)
# Register your models here.
