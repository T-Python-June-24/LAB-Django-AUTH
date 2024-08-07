# DrFahadHospital/urls.py
from django.contrib import admin
from django.urls import path, include
from main.views import index
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('clinics/', include('clinic.urls')),
    path('doctors/', include('doctor.urls')),
    path('reservations/', include('reservation.urls')),
    path('user/', include('user.urls')),
    path('staff/', include('staff.urls')),
    path('main/', include('main.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
