from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from doctors.models import Doctor
from clinics.models import Clinic
from datetime import datetime,timedelta
from django.template.loader import render_to_string
#from weasyprint import HTML
#from cryptography.fernet import Fernet
# Create your views here.



def home_view(request:HttpRequest):

    # products = Product.objects.all().order_by("product_name")
    # suppliers = Supplier.objects.all().order_by("supplier_name")
    # categories = Category.objects.all().order_by("name")


    # # Calculate the date 10 days from today
    # ten_days_from_today = datetime.now().date()+ timedelta(days=10)
    # # Filter products with expiry_date less than or equal to 10 days from today
    # ex_products = Product.objects.filter(expiry_date__lte=ten_days_from_today).order_by('product_name')

    # low_level_products = Product.objects.filter(stock_level__lte=10).order_by("product_name")

    clinics = Clinic.objects.all().order_by("name")[0:3]
    doctors = Doctor.objects.all()[0:3]
    
    return render(request, "main/index.html", {'clinics':clinics, 'doctors':doctors})



def mode_view(request:HttpRequest, mode):

    response = redirect(request.GET.get("next", "/"))

    if mode == "light":
        response.set_cookie("mode", "light")
    elif mode == "dark":
        response.set_cookie("mode", "dark")


    return response