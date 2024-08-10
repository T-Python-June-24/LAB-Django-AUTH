from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import login , logout , authenticate
from django.http import HttpRequest
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from Doctor.models import Doctor
from Reservation.models import Reservation
from Clinic.models import Clinic
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.admin.views.decorators import staff_member_required


# Create your views here.


def search(request: HttpRequest):
    if request.method == 'GET':
        type_search = request.GET.get('search_by', '')
        if type_search == 'doctor':
            word_search = request.GET.get('search_term', '')
            doctors = Doctor.objects.filter(full_name__icontains=word_search)
            count_product = doctors.count()
            return render(request, 'pages_admin/view_doctor.html', {
                'doctors': doctors,
                'count_product': count_product,
                'word_search': word_search
            })
        elif type_search == 'clinic':
            word_search = request.GET.get('search_term', '')
            clinics = Clinic.objects.filter(name__icontains=word_search)
            count_category = clinics.count()
            return render(request, 'pages_admin/view_clinic.html', {
                'clinics': clinics,
                'count_category': count_category,
                'word_search': word_search
            })
        elif  type_search =="reservation":
            word_search = request.GET.get('search_term', '')
            reservation = Reservation.objects.filter(Q(user__first_name__icontains=word_search) | Q(user__last_name__icontains=word_search))
            
            return render(request, 'pages_admin/view_reservation.html', {
                'reservation': reservation,
                
                'word_search': word_search
            })

def login_admin(request:HttpRequest):
    if request.method == 'POST':
        username=request.POST['username']
        password = request.POST['password']
        Verification = authenticate(request , username=username , password= password)
        if Verification  is not None and Verification.is_staff:
            login(request ,Verification )
            messages.success(request , f'welocome {username}')
            return redirect('ControlPanel:HomePanel')
        else:
            messages.error(request , 'The email or password is incorrect')
            return redirect('ControlPanel:login_admin')

    return render(request , 'pages_admin/sign_admin.html')

@staff_member_required(login_url='Home:Home')
def HomePanel(request:HttpRequest):
    count_doctor = Doctor.objects.count()
    count_clinic =  Clinic.objects.count()
    count_reservation = Reservation.objects.count()
    recent_reservation = Reservation.objects.all().order_by('-create_at')
    morning_clinic = Clinic.objects.filter(work_hours = 'morning')
    evening_clinic = Clinic.objects.filter(work_hours = 'EVENING')
    night_clinic = Clinic.objects.filter(work_hours = 'NIGHT')

    return render(request , 'pages_admin/Home.html' , {
        'count_doctor': count_doctor,
        'count_clinic': count_clinic,
        'count_reservation': count_reservation,
        'recent_reservation': recent_reservation,
        'morning_clinic': morning_clinic,
        'evening_clinic': evening_clinic,
        'night_clinic': night_clinic,
        })
@staff_member_required(login_url='Home:Home')
def view_doctor(request:HttpRequest):
    doctors = Doctor.objects.all()
    specializations = Doctor.Specializations.choices
    page_number = request.GET.get('page', 1)
    page_doctor = Paginator(doctors , 3)
    doctors_page = page_doctor.get_page(page_number)
    return render(request , 'pages_admin/view_doctor.html' ,{'doctors': doctors_page , 'specializations':specializations})
@staff_member_required(login_url='Home:Home')
def view_clinic(request:HttpRequest):
    clinics = Clinic.objects.all()
    work_hours = Clinic.WorkHours.choices
    page_number = request.GET.get('page', 1)
    page_clinic = Paginator(clinics , 3)
    clinics_page = page_clinic.get_page(page_number)
    doctor = Doctor.objects.all()
    return render(request , 'pages_admin/view_clinic.html' , {'clinics': clinics_page , "work_hours":work_hours , "doctor":doctor})

@staff_member_required(login_url='Home:Home')
def view_reservation(request:HttpRequest):
    reservation = Reservation.objects.all()
    page_number = request.GET.get('page', 1)
    page_clinic = Paginator(reservation , 10)
    reservation_page = page_clinic.get_page(page_number)
    return render(request , 'pages_admin/view_reservation.html' , {"reservation":reservation_page})