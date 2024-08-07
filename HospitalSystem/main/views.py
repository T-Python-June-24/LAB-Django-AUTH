from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def home_view(request:HttpRequest):

    return render(request, "index.html")

@login_required(login_url="account:log_in")
def dashboard_view(request:HttpRequest):

    return render(request, "dashboard.html")