from django.db import transaction, IntegrityError

from reservations.models import Reservation
from .models import Profile
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpRequest
from django.contrib import messages
from django.contrib.auth.decorators import login_required



def home(request: HttpRequest):
    return render(request, 'accounts/home.html')


def sign_up(request: HttpRequest):
    if request.method == 'POST':
        form_data = {
            'username': request.POST.get('username', ''),
            'first_name': request.POST.get('first_name', ''),
            'last_name': request.POST.get('last_name', ''),
            'email': request.POST.get('email', ''),
            'password': request.POST.get('password', ''),
            'phone_number': request.POST.get('phone_number', ''),
            'address': request.POST.get('address', ''),
            'user_image': request.FILES.get('user_image', None),
        }

        if not all([form_data['username'], form_data['password'], form_data['email']]):
            messages.error(request, 'Please fill in all required fields.')
            return render(request, 'accounts/signup.html', {'form_data': form_data})

        try:
            with transaction.atomic():
                if User.objects.filter(username=form_data['username']).exists():
                    messages.error(request, 'Username already exists')
                    return render(request, 'accounts/signup.html', {'form_data': form_data})

                new_user = User.objects.create_user(
                    username=form_data['username'],
                    first_name=form_data['first_name'],
                    last_name=form_data['last_name'],
                    email=form_data['email'],
                    password=form_data['password'],
                )

                Profile.objects.create(
                    user=new_user,
                    phone_number=form_data['phone_number'],
                    address=form_data['address'],
                    user_image=form_data['user_image'],
                )
                
                messages.success(request, 'Account created successfully')
                return redirect('accounts:sign_in')

        except IntegrityError as e:
            messages.error(request, f'Account creation failed due to database error: {e}')
        except Exception as e:
            messages.error(request, f'Account creation failed: {e}')
        
        return render(request, 'accounts/signup.html', {'form_data': form_data})

    return render(request, 'accounts/signup.html')


def sign_in(request: HttpRequest):
    next_url = request.GET.get('next', '/')
    if request.method == 'POST':
        try:
            user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                login(request, user)
                return redirect(next_url)
            else:
                messages.error(request, 'Invalid Login Attempt')
        except Exception as e:
            messages.error(request, f'Login failed: {e}')
    return render(request, 'accounts/login.html', {'next': next_url})

def log_out(request: HttpRequest):
    logout(request)
    return redirect('accounts:sign_in')



@login_required
def profile(request):
    user = request.user
    reservations = Reservation.objects.filter(user=user)
    return render(request, 'accounts/profile.html', {'user': user, 'reservations': reservations})



@login_required
def update_profile(request):
    if request.method == 'POST':
        user = request.user
        profile = user.profile
        
        user.username = request.POST.get('username', user.username)
        user.email = request.POST.get('email', user.email)
        
        profile.phone_number = request.POST.get('phone_number', profile.phone_number)
        profile.address = request.POST.get('address', profile.address)
        
        if 'user_image' in request.FILES:
            profile.user_image = request.FILES['user_image']
        
        try:
            user.save()
            profile.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('accounts:profile')  
        except Exception as e:
            messages.error(request, f'Profile update failed: {e}')
    
    return render(request, 'accounts/update_profile.html')


@login_required
def reservation_delete(request, pk):
    reservation = Reservation.objects.get(pk=pk)
    if request.method == 'POST':
        reservation.delete()
        return redirect('accounts:profile')
    return render(request, 'doctors/doctor_confirm_delete.html', {'reservation': reservation})
