from django.urls import path
from . import views
app_name = "TechnicianRoll"
urlpatterns = [
    path('dashboard/',views.technician_dashboard, name='technician_dashboard'),
    path('case-accepted/<int:id>/',views.case_accepted, name='case_accepted'),
]
