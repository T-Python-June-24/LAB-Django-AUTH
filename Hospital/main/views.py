from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from django.contrib import messages 
from clinics.models import Clinic
from doctors.models import Doctor
# Create your views here.
def home_view(request:HttpRequest):
    clinics = Clinic.objects.all()[0:3]
    doctors=Doctor.objects.all()[0:3]

    return render(request, 'main/index.html',{"clinics":clinics,"doctors":doctors})

def staff_dashboard(request):
    if not request.user.is_staff:
        messages.success(request, "only staff can view this page", "alert-warning")
        return redirect("main:home_view")
    
    return render(request, 'main/dashboard.html')
    
