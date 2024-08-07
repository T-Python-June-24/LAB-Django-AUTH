from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError, transaction
from django.contrib import messages
from .models import Profile

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
