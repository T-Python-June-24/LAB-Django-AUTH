from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError, transaction
from django.contrib import messages
from .models import Profile
from django.shortcuts import render, get_object_or_404

# Create your views here.


def sign_up(request: HttpRequest):
    if request.method == "POST":
        try:
            with transaction.atomic():
                new_user = User.objects.create_user(
                    username=request.POST["username"],
                    password=request.POST["password"],
                    email=request.POST["email"],
                    first_name=request.POST["first_name"],
                    last_name=request.POST["last_name"]
                )
                new_user.save()

                profile = Profile(
                    user=new_user,
                    phone_number=request.POST.get("phone_number"),
                    address=request.POST.get("address")
                )
                profile.save()

            messages.success(request, "Registered user successfully", extra_tags="alert-success")
            return redirect("users:sign_in")
        except Exception as e:
            messages.error(request, "Couldn't register user. Try again", extra_tags="alert-danger")
            print(e)
    return render(request, "users/signup.html")


def sign_in(request: HttpRequest):
    if request.method == "POST":

        # checking user credentials
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        print(user)
        if user:
            # login the user
            login(request, user)
            messages.success(request, "Logged in successfully", "alert-success")
            return redirect('main:index')
        else:
            messages.error(request, "Please try again. You credentials are wrong", "alert-danger")

    return render(request, "users/signin.html")


def log_out(request: HttpRequest):
    logout(request)
    messages.success(request, "Logged out successfully", "alert-warning")

    return redirect("main:index")


def user_profile(request, user_name):
    try:
        user = get_object_or_404(User, username=user_name)
        if not Profile.objects.filter(user=user).first():
            new_profile = Profile(user=user)
            new_profile.save()
    except Exception as e:
        print(e)

    return render(request, 'users/profile.html', {"user": user})


def update_user_profile(request: HttpRequest):
    if not request.user.is_authenticated:
        messages.warning(request, "Only registered users can update their profile", "alert-warning")
        return redirect("users:sign_in")

    if request.method == "POST":
        try:
            with transaction.atomic():
                user = request.user

                user.first_name = request.POST["first_name"]
                user.last_name = request.POST["last_name"]
                user.email = request.POST["email"]
                user.save()

                profile = user.profile
                profile.phone_number = request.POST.get("phone_number")
                profile.address = request.POST.get("address")
                profile.save()

                messages.success(request, "Updated profile successfully", "alert-success")
                return redirect("users:user_profile", user_name=user.username)
        except Exception as e:
            messages.error(request, "Couldn't update profile", "alert-danger")
            print(e)

    return render(request, "users/update_profile.html")
