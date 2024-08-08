# Notifications/utils.py
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings

def send_reservation_email(subject, html_template, context, recipient_list):
    html_content = render_to_string(html_template, context)
    text_content = f"Hello {context['username']}, your reservation at {context['clinic_name']} is confirmed for {context['reservation_date']}."

    email = EmailMultiAlternatives(
        subject,
        text_content,
        settings.EMAIL_HOST_USER,
        recipient_list
    )
    email.attach_alternative(html_content, "text/html")
    email.send()
