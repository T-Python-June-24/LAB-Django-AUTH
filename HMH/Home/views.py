from django.shortcuts import render , redirect
from django.http import HttpRequest
from Clinic.models import Clinic
from Doctor.models import Doctor
from Reservation.models import Reservation
from django.contrib import messages
from django.core.paginator import Paginator



# Create your views here.


def Home(request:HttpRequest):
    clinic = Clinic.objects.all()[:3]
    doctor = Doctor.objects.all()[:3]
    return render(request, 'pages/index.html', 
                  {'clinic':clinic , 
                   'doctor':doctor
                   })
    
def view_clinic(request:HttpRequest):
    clinic = Clinic.objects.all()
    page_number = request.GET.get('page', 1)
    page_clinic = Paginator(clinic , 3)
    clinic_page = page_clinic.get_page(page_number)
    return render(request , 'pages/clinic_page.html' , {'clinic':clinic_page})

def view_doctor(request:HttpRequest):
    doctor = Doctor.objects.all()
    page_number = request.GET.get('page', 1)
    page_doctor = Paginator(doctor , 3)
    doctor_page = page_doctor.get_page(page_number)
    return render(request , 'pages/doctor_page.html' , {'doctor':doctor_page})

def dector_detail(request:HttpRequest , doctor_name):
    doctor = Doctor.objects.get( full_name = doctor_name)
    clinics = Clinic.objects.filter(doctor=doctor)
    return render(request , 'pages/doctor_Detail.html' ,{'doctor':doctor , "clinics":clinics})

def clinic_detail(request:HttpRequest , clinic_name):
    cilnic=Clinic.objects.get(name=clinic_name)
    doctors = cilnic.doctor.all()
    Reservations = Reservation.objects.filter(clinic=cilnic, data=request.GET.get('data'))
    reservation_times = [reservation.time_slot.strftime('%H:%M') for reservation in Reservations]
    morning_times = ["07:00", "07:30", "08:00", "08:30", "09:00", "09:30", "10:00", "10:30", "11:00", "11:30", "12:00", "12:30", "13:00", "13:30", "14:00", "14:30", "15:00"]
    evening_times = ["15:00", "15:30", "16:00", "16:30", "17:00", "17:30", "18:00", "18:30", "19:00", "19:30", "20:00", "20:30", "21:00", "21:30", "22:00", "22:30", "23:00"]
    night_times = ["23:00", "23:30", "00:00", "00:30", "01:00", "01:30", "02:00", "02:30", "03:00", "03:30", "04:00", "04:30", "05:00", "05:30", "06:00", "06:30", "07:00"]
    print(reservation_times)
    return render(request , 'pages/clinic_detail.html' , {
        "cilnic":cilnic ,
          "doctors":doctors ,
            'Reserva':reservation_times,
            'morning_times':morning_times,
            'evening_times':evening_times,
            'night_times':night_times})


def profile(request: HttpRequest):
     if request.user.is_authenticated:
        user = request.user
        user_reservations = Reservation.objects.filter(user=user)
        
        return render(request, 'pages/profile.html', {
            'user': user,
            'reservations': user_reservations
        })
     messages.error(request , 'You must log in' , 'alert-danger')
     return redirect('login:sign_in')
def search(request:HttpRequest ):
    if request.method == 'GET':
        word_search = request.GET.get('query')
        doctor = Doctor.objects.filter(full_name__icontains = word_search)
        clinic = Clinic.objects.filter(name__icontains = word_search)
        return render(request , 'pages/doctor_page.html',{'doctor':doctor , 'clinic':clinic})
    return redirect("Home:view_doctor")
    