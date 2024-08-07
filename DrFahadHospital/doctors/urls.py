from django.urls import path
from .views import DoctorListView, DoctorDetailView, DoctorCreateView, DoctorUpdateView, DoctorDeleteView

urlpatterns = [
    path('', DoctorListView.as_view(), name='doctors'),
    path('<int:pk>/', DoctorDetailView.as_view(), name='doctor_detail'),
    path('new/', DoctorCreateView.as_view(), name='doctor_add'),
    path('<int:pk>/update/', DoctorUpdateView.as_view(), name='doctor_update'),
    path('<int:pk>/delete/', DoctorDeleteView.as_view(), name='doctor_delete'),
]
