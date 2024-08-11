from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from doctors.models import Doctor
from clinics.models import Clinic
from django.core.mail import send_mail
from django.contrib import messages
from django.core.files.storage import default_storage
from django.core.paginator import Paginator
from django.db.models import Q, F, Count, Avg, Sum, Min, Max



# Create your views here.


def all_doctors_view(request:HttpRequest, doctor_id):
    if doctor_id =="all":
        doctors = Doctor.objects.all().order_by("full_name")
    else:
        doctors  = Doctor.objects.filter(pk=doctor_id)
    
    page_number = request.GET.get('page',1)
    paginator = Paginator(doctors,6)
    doctors_page = paginator.get_page(page_number)

    return render(request, "doctors/all_doctors.html", {'doctors':doctors_page})



def doctor_detail_view(request:HttpRequest, doctor_id:int):

    doctor = Doctor.objects.get(pk=doctor_id)
    clinics = Clinic.objects.filter(doctors__id__in=[doctor_id])

    
    return render(request, "doctors/doctor_detail.html", {'doctor':doctor, 'clinics': clinics})
