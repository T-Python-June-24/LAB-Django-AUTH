# doctor/views.py
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Doctor


def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctor/doctor_list.html', {'doctors': doctors})


def doctor_detail(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    return render(request, 'doctor/doctor_detail.html', {'doctor': doctor})