from django.shortcuts import render, get_object_or_404
from .models import Doctor

def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctor/doctor_list.html', {'doctors': doctors})

def doctor_detail(request, doctor_id):
    doctor = get_object_or_404(Doctor, pk=doctor_id)
    return render(request, 'doctor/doctor_detail.html', {'doctor': doctor})

#def search_doctors(request):
    #query = request.GET.get('q')
    #results = Doctor.objects.filter(full_name__icontains