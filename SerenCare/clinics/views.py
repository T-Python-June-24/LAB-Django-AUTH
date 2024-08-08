from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from .models import Clinic,Doctor,Reservation
from django.core.mail import send_mail
import csv
from django.contrib import messages
from django.core.files.storage import default_storage
from django.core.paginator import Paginator
from django.db.models import Q, F, Count, Avg, Sum, Min, Max
from django.contrib import messages
from datetime import datetime, timedelta, time
from django.db import IntegrityError, transaction





def all_clinics_view(request:HttpRequest, clinic_id):
    if clinic_id =="all":
        clinics = Clinic.objects.all().order_by("name")
    else:
        clinics  = Clinic.objects.filter(pk=clinic_id)
    # products = Product.objects.filter(category__name = product_param).order_by("-expiry_date")
    # products = Product.objects.filter(suppliers__id__in=[product_param]).order_by("-expiry_date")
    # supplier  = Supplier.objects.filter(pk=product_param)
    page_number = request.GET.get('page',1)
    paginator = Paginator(clinics,6)
    clinics_page = paginator.get_page(page_number)

    return render(request, "clinics/all_clinics.html", {'clinics':clinics_page})



def clinic_detail_view(request:HttpRequest, clinic_id:int):

    clinic = Clinic.objects.get(pk=clinic_id)
    clinics = Clinic.objects.all()
    start_time = clinic.working_hours.start_time
    end_time = clinic.working_hours.end_time
    slots = []
    current_time = datetime.combine(datetime.today(), start_time)
    end_time = datetime.combine(datetime.today(), end_time)
    while current_time <= end_time:
        slots.append(current_time.time()) #time_slot.strftime('%H:%M:%S')
        current_time += timedelta(minutes=30)
    print(slots)

    # products = Product.objects.filter(category__name = product_param).order_by("-expiry_date")
    # products = Product.objects.filter(suppliers__id__in=[product_param]).order_by("-expiry_date")
    # supplier  = Supplier.objects.filter(pk=product_param)
    
    return render(request, "clinics/clinic_detail.html", {'clinic':clinic, 'clinics':clinics, 'slots':slots })



def reservation_view(request: HttpRequest):
    
    if request.user.is_authenticated:
        if request.method == "POST":
            clinic = Clinic.objects.get(pk=request.POST["clinic"])
            doctor = Doctor.objects.get(pk=request.POST["doctor"])
            try:
                with transaction.atomic():
                    new_reservation = Reservation.objects.create(user=request.user,clinic=clinic,doctor=doctor, date=request.POST["date"], time_slot=request.POST["time_slot"])
                    new_reservation.save()

                messages.success(request, "Your appointment was made successfuly", "alert-success")
                return redirect("main:home_view")
            
            except IntegrityError as e:
                messages.error(request, "Please check data integrity", "alert-danger")
            except Exception as e:
                messages.error(request, "Couldn't make an appointment. Please try again", "alert-danger")
                print(e)
    else:
         messages.error(request, "Only registerd patients can make an appointment. Please sign in/up", "alert-danger")  

    return redirect("main:home_view")


def delete_clinic_view(request:HttpRequest, clinic_id:int):
    try:
        clinic = Clinic.objects.get(pk=clinic_id)
        clinic.delete()
        messages.success(request, "Deleted clinic successfully", extra_tags='alert-success')
    except Exception as e:
        print(e)
        messages.error(request, "Can't delete clinic", extra_tags='alert-danger')
    return redirect("main:home_view")



def search_clinics_view(request:HttpRequest):

    if "search" in request.GET and len(request.GET["search"]) >= 2:
        clinics = Clinic.objects.filter(name__contains=request.GET["search"])

    else:
        clinins = []


    return render(request, "clinics/search_clinics.html", {"clinics" : clinics})

