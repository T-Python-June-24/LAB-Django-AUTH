from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

from django.contrib import messages

from .models import Reservation
from .forms import ReservationForm


# Create your views here.
def create(request:HttpRequest):

    if not (request.user.is_staff and request.user.has_perm("reservation.create")):
        messages.warning(request, "only staff can add reservations", "alert-warning")
        return redirect("main:home")
    
    if request.method == "POST":

        reservation_form = ReservationForm(request.POST, request.FILES)

        if reservation_form.is_valid():
            reservation_form.save()
        else:
            print(reservation_form.errors)

        return redirect("reservation:reservation_page")

    return render(request, "reservation/create.html")



def reservation_page(request:HttpRequest):

    return render(request, "reservation/reservation_page.html")