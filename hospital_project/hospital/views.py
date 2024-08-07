from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Clinic, Doctor, Reservation
from .forms import ReservationForm, ProfileForm
from django.core.paginator import Paginator
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView as BaseLoginView, LogoutView as BaseLogoutView
from django.contrib.auth import authenticate, login

# Create your views here.
def home(request):
    return render(request, 'home.html')

def clinic_list(request):
    clinics = Clinic.objects.all()
    paginator = Paginator(clinics, 10)  # Show 10 clinics per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'clinics': page_obj,
        'is_paginated': page_obj.has_other_pages(),
        'page_obj': page_obj,
        'paginator': paginator
    }
    return render(request, 'clinic_list.html', context)

def clinic_detail(request, clinic_id):
    clinic = get_object_or_404(Clinic, pk=clinic_id)
    doctors = clinic.doctors.all()
    reservation_form = ReservationForm()
    
    if request.method == 'POST':
        reservation_form = ReservationForm(request.POST)
        if reservation_form.is_valid():
            reservation = reservation_form.save(commit=False)
            reservation.user = request.user
            reservation.clinic = clinic
            reservation.save()
            messages.success(request, 'Reservation successfully made!')
            return redirect('clinic-detail', clinic_id=clinic_id)
    
    return render(request, 'clinic_detail.html', {
        'clinic': clinic,
        'doctors': doctors,
        'reservation_form': reservation_form,
    })

@login_required
def profile(request):
    profile = request.user.profile
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
    else:
        profile_form = ProfileForm(instance=profile)
    
    return render(request, 'profile.html', {'profile_form': profile_form})

@login_required
def reservations(request):
    user_reservations = Reservation.objects.filter(user=request.user)
    return render(request, 'reservations.html', {'user_reservations': user_reservations})

@user_passes_test(lambda u: u.is_staff)
def staff_dashboard(request):
    clinics = Clinic.objects.all()
    doctors = Doctor.objects.all()
    return render(request, 'staff_dashboard.html', {'clinics': clinics, 'doctors': doctors})

def doctor_list(request):
    doctors = Doctor.objects.all()
    paginator = Paginator(doctors, 10)  # Show 10 doctors per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'doctors': page_obj,
        'is_paginated': page_obj.has_other_pages(),
        'page_obj': page_obj,
        'paginator': paginator
    }
    return render(request, 'doctor_list.html', context)

def doctor_detail(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)
    context = {
        'doctor': doctor,
    }
    return render(request, 'doctor_detail.html', context)

class DoctorCreateView(CreateView):
    model = Doctor
    fields = ['full_name', 'specialization', 'bio', 'photo']
    template_name = 'doctor_form.html'
    success_url = reverse_lazy('staff-dashboard')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

class LoginView(BaseLoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('home')

class LogoutView(BaseLogoutView):
    next_page = reverse_lazy('home')
