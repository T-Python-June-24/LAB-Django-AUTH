from django.shortcuts import render , redirect
from .models import Clinic
from django.http import HttpRequest
from .forms import ClinitForm
from django.contrib import messages
# Create your views here.



def view_clinic(request:HttpRequest):
    views_clinic = Clinic.objects.all()
    return render(request , 'pages_clinic/view_clinic.html' , {'clinic':views_clinic})

def add_clinic(request:HttpRequest):
    referer = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        clinic_new = ClinitForm(request.POST , request.FILES)
        if clinic_new.is_valid():
            clinic_new.save()
            messages.success(request , 'done add Clinic')
            return redirect(referer)
        else:
            messages.error(request , f'not valid form {clinic_new.errors}')
            return redirect(referer)
    return redirect(referer)
def detaile_clinic(request:HttpRequest , id_clinic):
    clinic = Clinic.objects.get(id=id_clinic)
    return render(request , 'pages_clinic/detaile_clinic.html' , {'view_clinic': clinic})

def delete_clinic(request:HttpRequest , id_clinic):
    referer = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        del_clinic = Clinic.objects.get(pk = id_clinic)
        del_clinic.delete()
        messages.success(request , 'done delete clinic ') 
        return redirect(referer)
    messages.error(request , 'You did not pass any value')
    return redirect(referer)

def update_doctor(request:HttpRequest , id_clinic):
    referer = request.META.get('HTTP_REFERER')
    '''
    if not request.user.is_staff:
        messages.error(request , "only staff can add game")
        return redirect(referer)
        '''
    clinic = Clinic.objects.get(pk = id_clinic)
    
    if request.method == 'POST':
        clinic_form = ClinitForm(instance=clinic , data=request.POST , files=request.FILES)
        if clinic_form.is_valid:
            clinic_form.save()
            messages.success(request , 'done update doctor')
            return redirect(referer)
        else:
            messages.error(request , f'not valid form {clinic_form.errors}')
            return redirect(referer)
        
    messages.error(request , 'You did not pass any value')
    return redirect(referer)