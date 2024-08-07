# reservations/views.py
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def send_reservation_confirmation(user_email, reservation_details):
    send_mail(
        'Reservation Confirmation',
        f'Your reservation details: {reservation_details}',
        settings.DEFAULT_FROM_EMAIL,
        [user_email],
        fail_silently=False,
    )
def send_reservation_confirmation(user, reservation):
    subject = 'Reservation Confirmation'
    from_email = 'yourhospital@example.com'
    to_email = user.email
    html_content = render_to_string('emails/reservation_confirmation.html', {'user': user, 'reservation': reservation})
    text_content = strip_tags(html_content)
    email = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
    email.attach_alternative(html_content, "text/html")
    email.send()
    
    
class ReservationListView(ListView):
    model = Reservation
    template_name = 'reservations/reservations.html'
    context_object_name = 'reservations'

    def get_queryset(self):
        return Reservation.objects.filter(user=self.request.user)

class ReservationCreateView(CreateView):
    model = Reservation
    form_class = ReservationForm
    template_name = 'reservations/reservation_form.html'
    success_url = '/reservations/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)