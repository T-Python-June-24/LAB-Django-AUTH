from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Doctor
from .forms import DoctorForm

class DoctorListView(ListView):
    model = Doctor
    template_name = 'doctors/doctors.html'
    context_object_name = 'doctors'
    paginate_by = 6

class DoctorDetailView(DetailView):
    model = Doctor
    template_name = 'doctors/doctor_detail.html'

class DoctorCreateView(CreateView):
    model = Doctor
    form_class = DoctorForm
    template_name = 'doctors/doctor_form.html'
    success_url = '/doctors/'

class DoctorUpdateView(UpdateView):
    model = Doctor
    form_class = DoctorForm
    template_name = 'doctors/doctor_form.html'
    success_url = '/doctors/'

class DoctorDeleteView(DeleteView):
    model = Doctor
    template_name = 'doctors/doctor_confirm_delete.html'
    success_url = '/doctors/'
