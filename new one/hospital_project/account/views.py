from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import RegistrationForm ,LoginForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from clinic.models import Clinic
from doctor.models import Doctor
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, "Registered User Successfuly", "alert-success")
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()
        print('Registration x')
    return render(request, 'account/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                print('valid username or password')
                messages.success(request, "Registered User Successfuly", "alert-success")
                return redirect('home')  
    else:
        form = LoginForm()
        messages.error(request, "Please try again", "alert-danger")

    return render(request, 'account/login.html', {'form': form})


def home(request):
    clinics = Clinic.objects.all()[:3]  
    doctors = Doctor.objects.all()[:3]  
    return render(request, 'home.html', {'clinics': clinics, 'doctors': doctors})

def user_logout(request):
    logout(request)
    return redirect('login') 


@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user)
    return render(request, 'account/profile.html', {'form': form})