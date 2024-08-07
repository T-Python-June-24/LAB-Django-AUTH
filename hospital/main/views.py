from django.shortcuts import render ,redirect
from django.http import HttpRequest ,Http404
from doctor.models import Doctor
from clinic.models import Clinic
from django.contrib import messages
# Create your views here.
def home_view(request:HttpRequest):
    doctors=Doctor.objects.all()[0:4]
    print(Doctor.objects.get(pk=1).clinic_set.all())
    clinics=Clinic.objects.all()[0:4]
    return render(request,'main/home.html',{'doctors':doctors,"clinics":clinics})
def sttaf_view(request:HttpRequest):
    if request.user.is_staff:
        return render(request,"main/sttaf.html")
    else :
        return redirect("main:home_view")
    
def add_doctor_view(request:HttpRequest):
    if request.user.is_staff:
        if request.method=="POST":
            doctor=Doctor(full_name=request.POST['name'],specilaization=request.POST['specilaization'],bio=request.POST['bio'], photo=request.FILES.get("image", Doctor.photo.field.get_default()))
            doctor.save()
            messages.success(request,f"Doctor {doctor.full_name} Added successfully",'green')
        return render(request,"main/add_doctor.html")
    else :
        return redirect("main:home_view")
    
def add_clinic_view(request:HttpRequest):
    if request.user.is_staff:

        print(request.POST)
        if request.method=="POST":
            clinic=Clinic(name=request.POST['name'],description=request.POST['description'],working_hours=request.POST["working_hours"])
            clinic.save()
            clinic.doctor.set(request.POST.getlist("doctor"))
            messages.success(request,f"{clinic.name} added successfully","green")
        doctors=Doctor.objects.all()
        return render(request,"main/add_clinic.html",{"doctors":doctors,"working_hours":Clinic.WorkingHours.choices} )
    else :
        return redirect("main:home_view")