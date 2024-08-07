import random
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from accounts.models import Profile
from clinics.models import Clinic
from doctors.models import Doctor
from reservations.models import Reservation
from django.utils import timezone
from datetime import timedelta

class Command(BaseCommand):
    help = 'Seed the database with sample data'

    def handle(self, *args, **options):
        self.stdout.write('Seeding data...')

        # Create superuser
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'adminpassword')
            self.stdout.write(self.style.SUCCESS('Superuser created'))

        # Create clinics
        clinic_data = [
            {
                'name': 'City General Hospital',
                'description': 'A leading general hospital in the city center.',
                'opening_time': '08:00',
                'closing_time': '20:00',
                'feature_image': 'https://example.com/city_general_hospital.jpg'
            },
            {
                'name': 'Sunset Medical Center',
                'description': 'Specialized care in a comfortable setting.',
                'opening_time': '09:00',
                'closing_time': '17:00',
                'feature_image': 'https://example.com/sunset_medical_center.jpg'
            },
            {
                'name': 'Riverside Clinic',
                'description': 'Family-oriented healthcare by the river.',
                'opening_time': '08:00',
                'closing_time': '20:00',
                'feature_image': 'https://example.com/riverside_clinic.jpg'
            },
        ]

        for data in clinic_data:
            Clinic.objects.get_or_create(name=data['name'], defaults=data)

        self.stdout.write(self.style.SUCCESS('Clinics created'))

        # Create doctors
        doctor_data = [
            {
                'full_name': 'Dr. John Smith',
                'specialization': 'CARDIOLOGY',
                'bio': 'Experienced cardiologist with over 15 years of practice.',
                'photo': 'https://example.com/dr_john_smith.jpg'
            },
            {
                'full_name': 'Dr. Emily Johnson',
                'specialization': 'DERMATOLOGY',
                'bio': 'Specializing in advanced skincare treatments.',
                'photo': 'https://example.com/dr_emily_johnson.jpg'
            },
            {
                'full_name': 'Dr. Michael Lee',
                'specialization': 'NEUROLOGY',
                'bio': 'Dedicated to neurological research and patient care.',
                'photo': 'https://example.com/dr_michael_lee.jpg'
            },
        ]

        for data in doctor_data:
            doctor, created = Doctor.objects.get_or_create(full_name=data['full_name'], defaults=data)
            if created:
                # Assign doctor to a random clinic
                clinic = Clinic.objects.order_by('?').first()
                doctor.clinics.add(clinic)

        self.stdout.write(self.style.SUCCESS('Doctors created and assigned to clinics'))

        # Create regular users with profiles
        user_data = [
            {
                'username': 'patient1',
                'email': 'patient1@example.com',
                'password': 'patientpass1',
                'profile': {
                    'phone_number': '123-456-7890',
                    'address': '123 Main St, Anytown, USA',
                    'date_of_birth': '1990-01-01',
                    'profile_picture': 'https://example.com/patient1_profile.jpg'
                }
            },
            {
                'username': 'patient2',
                'email': 'patient2@example.com',
                'password': 'patientpass2',
                'profile': {
                    'phone_number': '098-765-4321',
                    'address': '456 Oak Ave, Another Town, USA',
                    'date_of_birth': '1985-05-15',
                    'profile_picture': 'https://example.com/patient2_profile.jpg'
                }
            },
        ]

        for data in user_data:
            user, created = User.objects.get_or_create(username=data['username'], defaults={'email': data['email']})
            if created:
                user.set_password(data['password'])
                user.save()
                profile, _ = Profile.objects.get_or_create(user=user)
                profile.phone_number = data['profile']['phone_number']
                profile.address = data['profile']['address']
                profile.date_of_birth = data['profile']['date_of_birth']
                profile.profile_picture = data['profile']['profile_picture']
                profile.save()

        self.stdout.write(self.style.SUCCESS('Users created with profiles'))

        # Create sample reservations
        users = User.objects.filter(username__startswith='patient')
        clinics = Clinic.objects.all()
        doctors = Doctor.objects.all()

        for _ in range(5):  # Create 5 sample reservations
            user = random.choice(users)
            clinic = random.choice(clinics)
            doctor = random.choice(clinic.doctors.all())
            date = timezone.now().date() + timedelta(days=random.randint(1, 30))
            time_slot = f"{random.randint(9, 16):02d}:00"
            
            Reservation.objects.create(
                user=user,
                clinic=clinic,
                doctor=doctor,
                date=date,
                time_slot=time_slot
            )

        self.stdout.write(self.style.SUCCESS('Sample reservations created'))

        self.stdout.write(self.style.SUCCESS('Data seeding completed successfully'))
