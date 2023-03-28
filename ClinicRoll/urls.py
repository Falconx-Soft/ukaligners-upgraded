from django.urls import path
from . import views
app_name = "ClinicRoll"
urlpatterns = [
    path('dashboard/',views.clinic_dashboard, name='clinic_dashboard'),
]
