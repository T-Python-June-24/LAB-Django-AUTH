from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from .models import Doctor
from .forms import DoctorForm
from django.contrib import messages 
from django.core.paginator import Paginator


# Create your views here.

def add_doctor(request:HttpRequest):
    if request.method=="POST":
        doctorForm=DoctorForm(request.POST,request.FILES)
        if doctorForm.is_valid():
            doctorForm.save()
            messages.success(request, 'doctor added successfully!','alert-success')
            return redirect("doctors:doctor_view")
        else:    
            for field, errors in doctorForm.errors.items():
                 for error in errors:
                     messages.error(request, f"{field}: {error}",'alert-danger')
    return render(request, "doctors/add_doctors.html",{"specialization":Doctor.Specialization.choices})        

def delete_doctor(request:HttpRequest,doctor_id):
     
     doctor = Doctor.objects.get(pk=doctor_id)
     if doctor.delete():
             messages.success(request, 'doctor deleted successfully!',"alert-success")
             return redirect('doctors:doctor_view')
     else:
         for field, errors in doctor.errors.items():
             for error in errors:
                 messages.error(request, f"{field}: {error}","alert-danger")    
     return redirect('doctors:doctor_view')
def update_doctor(request:HttpRequest,doctor_id):
     doctor = Doctor.objects.get(pk=doctor_id)
     if request.method == "POST":
         doctorForm=DoctorForm(request.POST, request.FILES, instance=doctor)
         if doctorForm.is_valid():
             doctorForm.save()
             messages.success(request, 'doctor updated successfully!',"alert-success")
             return redirect('doctors:doctor_view')
         else:
             for field, errors in doctorForm.errors.items():
                 for error in errors:
                     messages.error(request, f"{field}: {error}","alert-danger")
         print(Doctor.Specialization.choices)
     return render(request, "doctors/doctor_view.html", {'doctorForm': doctorForm, 'doctor': doctor, 'specialization': Doctor.Specialization.choices})
      
def doctor_view(request:HttpRequest):
    doctors = Doctor.objects.all() 

    # Check if a search was made
    searched = request.GET.get('searched', '')
    if searched:
        doctors = doctors.filter(full_name__icontains=searched)


    page_number = request.GET.get("page", 1)
    paginator = Paginator(doctors, 6)
    doctors = paginator.get_page(page_number)
    if request.user.is_staff:
     return render(request, "doctors/doctor_view.html", {"doctors" : doctors,'specialization': Doctor.Specialization.choices, "search_term": searched,
})
    else:
     return render(request, "doctors/user_doctor_view.html", {"doctors" : doctors,'specialization': Doctor.Specialization.choices,"search_term": searched,
})


def doctor_detail(request:HttpRequest,doctor_id:int):
    doctor = Doctor.objects.get(pk=doctor_id)
    return render(request, "doctors/doctor_detail.html",{"doctor": doctor})

