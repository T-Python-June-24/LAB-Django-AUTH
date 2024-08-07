from django.shortcuts import render
from django.http import HttpRequest
from .models import Clinic
# Create your views here.
def clinic_page(request:HttpRequest,clinic_id):
    clinic=Clinic.objects.get(pk=clinic_id)
    return render(request,"clinic/clinic_page.html",{"clinic":clinic})