from django.shortcuts import render
from django.http import HttpRequest
# Create your views here.


def Home(request:HttpRequest):
    return render(request, 'pages/index.html')