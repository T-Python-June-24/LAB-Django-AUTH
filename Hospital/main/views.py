from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from clinics.models import Clinic
from doctors.models import Doctor


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    clinics = Clinic.objects.all()[0:3]
    doctors = Doctor.objects.all()[0:3]

    return render(request, 'main/index.html', {"clinics": clinics, "doctors": doctors})
