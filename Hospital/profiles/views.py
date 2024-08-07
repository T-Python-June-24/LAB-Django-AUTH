from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError, transaction
from django.contrib import messages
from .models import Profile
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

def sign_up(request: HttpRequest):
    if request.method == "POST":
        password = request.POST.get("password")
        password_confirmation = request.POST.get("password_confirmation")

        if password != password_confirmation:
            messages.error(request, "Passwords do not match!", extra_tags="alert-danger")
            return render(request, "profiles/signup.html", {})

        try:
            with transaction.atomic():
                new_user = User.objects.create_user(
                    username=request.POST["username"],
                    password=password,  # Use the password variable here
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

            messages.success(request, "Registered User Successfully", extra_tags="alert-success")
            return redirect("profiles:sign_in")


        except Exception as e:
            messages.error(request, "Couldn't register user. Try again", extra_tags="alert-danger")
            print(e)

    return render(request, "profiles/signup.html", {})



def sign_in(request:HttpRequest):

    if request.method == "POST":

        #checking user credentials
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        print(user)
        if user:
            #login the user
            login(request, user)
            messages.success(request, "Logged in successfully", "alert-success")
            return redirect(request.GET.get("next", "/"))
        else:
            messages.error(request, "Please try again. You credentials are wrong", "alert-danger")



    return render(request, "profiles/signin.html")


def log_out(request: HttpRequest):

    logout(request)
    messages.success(request, "logged out successfully", "alert-warning")

    return redirect("main:home_view")




@login_required
def user_profile_view(request, user_name):
    # Check if the requested username is the same as the logged-in user's username
    if request.user.username != user_name:
        return HttpResponse("Unauthorized", status=401)

    user = get_object_or_404(User, username=user_name)
    profile, created = Profile.objects.get_or_create(user=user)
    if created:
        profile.save()

    return render(request, 'profiles/profile.html', {"user": user, "profile": profile})

def update_user_profile(request: HttpRequest):
    if not request.user.is_authenticated:
        messages.warning(request, "Only registered users can update their profile", "alert-warning")
        return redirect("profiles:sign_in")

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

                messages.success(request, "Profile updated successfully", "alert-success")
                return redirect("profiles:user_profile_view", user_name=user.username)

        except Exception as e:
            messages.error(request, "Couldn't update profile", "alert-danger")
            print(e)

    return render(request, "profiles/update_profile.html")