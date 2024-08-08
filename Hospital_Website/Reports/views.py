from django.shortcuts import render
from accounts.models import Profile
from clinics.models import Clinic
from doctors.models import Doctor
from reservations.models import Reservation
import plotly.graph_objs as go
from django.contrib.auth.models import User
import json
from django.db.models.functions import TruncMonth
from django.db.models import Count
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    # Total counts
    total_admins = User.objects.filter(is_superuser=True).count()
    total_staff = User.objects.filter(is_staff=True).count()
    total_users = Profile.objects.count()
    total_clinics = Clinic.objects.count()
    total_doctors = Doctor.objects.count()
    total_reservations = Reservation.objects.count()

    # Most and least popular clinics
    most_popular_clinic = Clinic.objects.annotate(total_reservations=Count('reservation')).order_by('-total_reservations').first()
    least_popular_clinic = Clinic.objects.annotate(total_reservations=Count('reservation')).order_by('total_reservations').first()

    # Most and least popular doctors
    most_popular_doctor = Doctor.objects.annotate(total_reservations=Count('reservation')).order_by('-total_reservations').first()
    least_popular_doctor = Doctor.objects.annotate(total_reservations=Count('reservation')).order_by('total_reservations').first()

    monthly_reservations = Reservation.objects.annotate(month=TruncMonth('reservation_date')).values('month').annotate(total_reservations=Count('id')).order_by('month')
    monthly_reservations_labels = [res['month'].strftime('%b %Y') for res in monthly_reservations]
    monthly_reservations_labels_card = [res['month'].strftime('%b %Y') for res in monthly_reservations]

    monthly_reservations_data = [res['total_reservations'] for res in monthly_reservations]

    total_data = [go.Bar(
        x=['Clinics', 'Doctors', 'Reservations'],
        y=[total_clinics, total_doctors, total_reservations],
    )]

    category_labels = ['Admins', 'Staff', 'Users']
    category_data = [total_admins, total_staff, total_users]

    context = {
        'total_clinics': total_clinics,
        'total_doctors': total_doctors,
        'total_users': total_users,
        'total_admins': total_admins,
        'total_staff': total_staff,
        'total_reservations': total_reservations,
        'most_popular_clinic': most_popular_clinic.name if most_popular_clinic else 'N/A',
        'least_popular_clinic': least_popular_clinic.name if least_popular_clinic else 'N/A',
        'most_popular_doctor': most_popular_doctor.full_name if most_popular_doctor else 'N/A',
        'least_popular_doctor': least_popular_doctor.full_name if least_popular_doctor else 'N/A',
        'total_data': json.dumps([trace.to_plotly_json() for trace in total_data]),
        'monthly_reservations_labels': json.dumps(monthly_reservations_labels),
        'monthly_reservations_labels_card': monthly_reservations_labels_card,  #! For the card
        'monthly_reservations_data': json.dumps(monthly_reservations_data),
        'category_labels': json.dumps(category_labels),
        'category_data': json.dumps(category_data),
    }

    return render(request, 'Reports/dashboard.html', context)
