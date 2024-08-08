from django.shortcuts import render ,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login , logout , authenticate
from django.http import HttpRequest
from django.contrib import messages
from .models import Profile
# Create your views here.


def sign_up(request:HttpRequest):
    if request.method == 'POST':
        phone_number = request.POST['phone_number']
        address = request.POST['address']
        create_user = User.objects.create_user(username=request.POST['username'] , first_name = request.POST['first_name'] , last_name =request.POST['last_name'], password=request.POST['password'], email=request.POST['email'])
        info_profile=Profile(user=create_user , phone_number=phone_number , address = address)
        info_profile.save()
        create_user.save()
        messages.success(request , 'Account successfully created')
        return redirect('login:sign_in')
    return render(request, 'pages_sign/sign_up.html')

def sign_in(request:HttpRequest):
    if request.method == 'POST':
        username=request.POST['username']
        password = request.POST['password']
        Verification = authenticate(request , username=username , password= password)
        if Verification:
            login(request ,Verification )
            messages.success(request , f'welocome {username}')
            return redirect('Home:Home')
        else:
            messages.error(request , 'The email or password is incorrect')
            return redirect('login:sign_in')

    return render(request , 'pages_sign/sign_in.html')


def update_user(request:HttpRequest , user_id):
    referer = request.META.get('HTTP_REFERER')
    user = User.objects.get(pk = user_id)
    profile=Profile.objects.get(user=user)
    if request.method == 'POST':
        user.username = request.POST['username']
        user.email = request.POST['email']
        user.first_name  = request.POST['first_name']
        user.last_name = request.POST['last_name']
        profile.phone_number =  request.POST['phone_number']
        profile.address = request.POST['address']
        user.save()
        profile.save()
        messages.success(request , 'done')
        return redirect(referer)

def logout_user(request:HttpRequest):
    logout(request)
    return redirect('Home:Home')