from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError, transaction
from django.contrib import messages
from .models import Profile
from reservations.models import Reservation

# Create your views here.

def sign_up(request: HttpRequest):

    if request.method == "POST":
        try:
            with transaction.atomic():
                # Create the user
                new_user = User.objects.create_user(
                    username=request.POST["username"],
                    password=request.POST["password"],
                    email=request.POST["email"],
                )
                new_user.save()

                # Create profile for the user
                profile = Profile(
                    user=new_user,
                    phone_number=request.POST["phone_number"],
                    address=request.POST["address"]
                )
                profile.save()

            messages.success(request, "Registered User Successfully")
            return redirect("accounts:sign_in")

        except IntegrityError:
            messages.error(request, "Please choose another username")
        except Exception as e:
            messages.error(request, "Couldn't register user. Try again")
            print(e)

    return render(request, "accounts/signup.html", {})


def sign_in(request: HttpRequest):

    if request.method == "POST":
        # Checking user credentials
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        print(user)
        if user:
            # Log in the user
            login(request, user)
            messages.success(request, "Logged in successfully")
            return redirect(request.GET.get("next", "/"))
        else:
            messages.error(request, "Please try again. Your credentials are wrong")

    return render(request, "accounts/signin.html")


def log_out(request: HttpRequest):
    logout(request)
    messages.success(request, "Logged out successfully")

    return redirect(request.GET.get("next", "/"))


def profile_view(request: HttpRequest):
    # Check if the user is authenticated
    if not request.user.is_authenticated:
        messages.error(request, "You need to be logged in to view this page.")
        return redirect('accounts:sign_in')

    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        messages.error(request, "Profile not found.")
        return redirect('accounts:sign_in')

    # Get reservations for the logged-in user
    reservations = Reservation.objects.filter(user=request.user).order_by('-date', '-time_slot')

    return render(request, 'accounts/profile.html', {
        'profile': profile,
        'reservations': reservations
    })


def edit_profile_view(request: HttpRequest):
    profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')

        # Update user information
        request.user.email = request.POST.get('email')
        request.user.save()

        # Update profile information
        profile.phone_number = phone_number
        profile.address = address
        profile.save()

        messages.success(request, "Profile updated successfully!")
        return redirect('accounts:profile')

    return render(request, 'accounts/edit_profile.html', {'profile': profile})

