from django.shortcuts import render ,redirect
from django.http import HttpRequest
from .models import Profile
from django.contrib.auth.models import User
from django.contrib import messages
from django.db import  transaction
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def signup_view(request:HttpRequest):
    try:
     with transaction.atomic():
        if request.method=="POST":
            username=request.POST.get("user_name")
            user=User.objects.create_user(username=username,first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'],password=request.POST['password'])
            user.save()
            uploaded_image = request.FILES.get('image', None)
            if uploaded_image is None:
                uploaded_image = Profile._meta.get_field('image').get_default()
            profile=Profile(user=user,phone_number=request.POST['phone_number'],address=request.POST['address'],image=uploaded_image,)
            profile.save()
            messages.success(request,"Signed up successfully","green")
            return redirect("main:home_view")
    except Exception as e:
        messages.error(request,"invalid email or password","red")
        print(e)
    return render(request,'registration/signup.html')
def login_view(request:HttpRequest):
    
    if request.method=="POST":
        user = authenticate(request,username=request.POST['user_name'], password=request.POST['password'])
        if user is not None:
                login(request,user)
                messages.success(request,"singed in successfully",'green')
                return redirect("main:home_view")
        else:
                messages.error(request,"invalid password or email",'red')
                
    return render(request,'registration/login.html')
def logout_view(request:HttpRequest):
    try:
        logout(request)
        messages.success(request,"logged Out successfully",'green')
        return redirect("main:home_view")
    except Exception as e:
        messages.error(request,"Something went wrong can't logout",'red')
def profile_view(request:HttpRequest,user_name):
    if request.user.username==user_name:

        try:
            user = User.objects.get(username=user_name)
            reservations=user.reservation_set.all()

            if not Profile.objects.filter(user=user).first():
                new_profile = Profile(user=user)
                new_profile.save()
            
        except Exception as e:
            print(e)
            return render(request,'404.html')
    else:
        return render(request,'404.html')
    

    return render(request, 'registration/profile.html', {"myuser" : user_name,'reservations':reservations})

def edit_profile(request:HttpRequest,user_name):
    
    try:
     with transaction.atomic():
        
        if request.method=="POST":
            user=User.objects.filter(username=user_name).first()
            user.username=request.POST['user_name']
            user.first_name=request.POST['first_name']
            user.last_name=request.POST['last_name']
            user.save()
            profile=Profile.objects.filter(user=user).first()
            profile.image = request.FILES.get('image', None)
            profile.address=request.POST['address']
            profile.save()
            messages.success(request,"updated successfully","green")
            return redirect("main:home_view")
    except Exception as e:
        messages.error(request,"something went wrong","red")
        print(e,"the erorr")

    return render(request,"registration/edit_profile.html",{"user":User.objects.filter(username=user_name).first()})
