# main/urls.py
from django.urls import path, include
from .views import index, search_results

urlpatterns = [
    path('', index, name='home'),
    path('clinic/', include('clinic.urls')),
    path('doctor/', include('doctor.urls')),
    path('reservation/', include('reservation.urls')),
    path('user/', include('user.urls')),
    path('staff/', include('staff.urls')),
    path('', search_results, name='search_results'), 
]
