from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse


from django.db.models import Count
from .models import Contact
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib import messages


def home(request:HttpRequest):

    if request.user.is_authenticated:
        print(request.user.email)
    else:
        print("User is not logged in")

    
    return render(request, 'main/home.html')


def contact(request:HttpRequest):

    if request.method == "POST":
        contact = Contact(name=request.POST["name"], email=request.POST["email"], message=request.POST["message"])
        contact.save()

        #send confirmation email
        content_html = render_to_string("main/mail/confirmation.html")
        send_to = contact.email
        email_message = EmailMessage("confiramation", content_html, settings.EMAIL_HOST_USER, [send_to])
        email_message.content_subtype = "html"
        #email_message.connection = email_message.get_connection(True)
        email_message.send()

        messages.success(request, "Your message is received. Thank You.", "alert-success")


    return render(request, 'main/contact.html' )

def mode_view(request:HttpRequest, mode):

    response = redirect(request.GET.get("next", "/"))

    if mode == "light":
        response.set_cookie("mode", "light")
    elif mode == "dark":
        response.set_cookie("mode", "dark")


    return response