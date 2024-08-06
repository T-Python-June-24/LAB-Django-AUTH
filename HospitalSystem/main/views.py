from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from doctors.models import Doctor


def home_view(request:HttpRequest):

    doctors = Doctor.objects.all()[0:3]


    return render(request, 'main/index.html',{"doctors":doctors,'specialization_choices': Doctor.SpecializationChoices.choices})

