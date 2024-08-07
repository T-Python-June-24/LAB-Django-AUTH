from django.urls import path
from .views import ClinicListView, ClinicDetailView, ClinicCreateView, ClinicUpdateView, ClinicDeleteView

urlpatterns = [
    path('', ClinicListView.as_view(), name='clinics'),
    path('<int:pk>/', ClinicDetailView.as_view(), name='clinic_detail'),
    path('new/', ClinicCreateView.as_view(), name='clinic_add'),
    path('<int:pk>/update/', ClinicUpdateView.as_view(), name='clinic_update'),
    path('<int:pk>/delete/', ClinicDeleteView.as_view(), name='clinic_delete'),
]
