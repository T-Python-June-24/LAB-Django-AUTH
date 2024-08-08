from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from .models import Clinic
from .forms import ClinicForm
from django.contrib import messages 
from doctors.models import Doctor
from django.core.paginator import Paginator

# Create your views here.

def add_clinic(request):
    doctors = Doctor.objects.all()
    if request.method=="POST":
        clinicForm=ClinicForm(request.POST,request.FILES)
        if clinicForm.is_valid():
            clinicForm.save()
            messages.success(request, 'Clinic added successfully!','alert-success')
            return redirect("clinics:clinic_view")
        else:    
            for field, errors in clinicForm.errors.items():
                 for error in errors:
                     messages.error(request, f"{field}: {error}",'alert-danger')
    return render(request, "clinics/add_clinic.html",{'doctors':doctors})        

def delete_clinic(request,clinic_id):
     
     clinic = Clinic.objects.get(pk=clinic_id)
     if clinic.delete():
             messages.success(request, 'clinic deleted successfully!',"alert-success")
             return redirect('clinics:clinic_view')
     else:
         for field, errors in clinic.errors.items():
             for error in errors:
                 messages.error(request, f"{field}: {error}","alert-danger")    
     return redirect('clinics:clinic_view')


def update_clinic(request,clinic_id):
     clinic = Clinic.objects.get(pk=clinic_id)
     doctors=Doctor.objects.all()
     if request.method == "POST":
         clinicForm=ClinicForm(request.POST, request.FILES, instance=clinic)
         if clinicForm.is_valid():
             clinicForm.save()
             messages.success(request, 'clinic updated successfully!',"alert-success")
             return redirect('clinics:clinic_view')
         else:
             for field, errors in clinicForm.errors.items():
                 for error in errors:
                     messages.error(request, f"{field}: {error}","alert-danger")
     return render(request, 'clinics/update_clinic.html', {'clinicForm': clinicForm, 'clinic': clinic,'doctors':doctors})
      
def clinic_view(request):

    clinics = Clinic.objects.all()
    doctors=Doctor.objects.all()

    # Check if a search was made
    searched = request.GET.get('searched', '')
    if searched:
        clinics = clinics.filter(name__icontains=searched)


    page_number = request.GET.get("page", 1)
    paginator = Paginator(clinics, 6)
    clinics = paginator.get_page(page_number)

    if request.user.is_staff:
     return render(request, "clinics/clinic_view.html", {"clinics" : clinics,"doctors":doctors,"search_term": searched})
    if not request.user.is_staff:

      return render(request, "clinics/user_clinic_view.html", {"clinics" : clinics ,"search_term": searched })

def clinic_detail(request,clinic_id):
     clinic = Clinic.objects.get(pk=clinic_id)
     doctors=clinic.doctors.all()
     return render(request, "Clinics/clinic_detail.html",{"clinic":clinic , "doctors":doctors})


    