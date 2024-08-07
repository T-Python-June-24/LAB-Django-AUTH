from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Clinic
from .forms import ClinicForm

class ClinicListView(ListView):
    model = Clinic
    template_name = 'clinics/clinics.html'
    context_object_name = 'clinics'
    paginate_by = 6

class ClinicDetailView(DetailView):
    model = Clinic
    template_name = 'clinics/clinic_detail.html'

class ClinicCreateView(CreateView):
    model = Clinic
    form_class = ClinicForm
    template_name = 'clinics/clinic_form.html'
    success_url = '/clinics/'

class ClinicUpdateView(UpdateView):
    model = Clinic
    form_class = ClinicForm
    template_name = 'clinics/clinic_form.html'
    success_url = '/clinics/'

class ClinicDeleteView(DeleteView):
    model = Clinic
    template_name = 'clinics/clinic_confirm_delete.html'
    success_url = '/clinics/'
