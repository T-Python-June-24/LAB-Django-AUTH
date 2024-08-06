from django.shortcuts import render ,redirect
from django.http import HttpRequest
from .models import Doctor
from django.contrib import messages
from .forms import DoctorForm
# Create your views here.

def view_doctor(request:HttpRequest):
    views_doctor = Doctor.objects.all()
    specializations = Doctor.Specializations.choices
    
    return render(request , 'pages_doctor/view_doctor.html' , {'doctor':views_doctor , 'specializations':specializations})

def add_doctor(request:HttpRequest):
    if request.method == 'POST':
        doctor_new = DoctorForm(request.POST , request.FILES)
        if doctor_new.is_valid:
            doctor_new.save()
            messages.success(request , 'done add Doctor')
            return redirect('Doctor:view_doctor')
        else:
            messages.error(request , f'not valid form {doctor_new.errors}')
            return redirect('Doctor:view_doctor')
    return redirect('Doctor:view_doctor')
def detaile_doctor(request:HttpRequest , id_doctor):
    doctor = Doctor.objects.get(id=id_doctor)
    return render(request , 'pages_doctor/detaile_doctor.html' , {'view_doctor': doctor})

def delete_doctor(request:HttpRequest , id_doctor):
    referer = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        del_doctor = Doctor.objects.get(pk = id_doctor)
        del_doctor.delete()
        messages.success(request , 'done delete doctor ') 
        return redirect(referer)
    messages.error(request , 'You did not pass any value')
    return redirect(referer)

def update_doctor(request:HttpRequest , id_doctor):
    referer = request.META.get('HTTP_REFERER')
    if not request.user.is_staff:
        messages.error(request , "only staff can add game")
        return redirect(referer)
    doctor = Doctor.objects.get(pk = id_doctor)
    
    if request.method == 'POST':
        doctor_form = DoctorForm(instance=doctor , data=request.POST , files=request.FILES)
        if doctor_form.is_valid:
            doctor_form.save()
            messages.success(request , 'done update doctor')
            return redirect(referer)
        else:
            messages.error(request , f'not valid form {doctor_form.errors}')
            return redirect(referer)
        
    messages.error(request , 'You did not pass any value')
    return redirect(referer)