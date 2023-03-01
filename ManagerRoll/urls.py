from django.urls import path
from . import views
app_name = "ManagerRoll"
urlpatterns = [
    path('dashboard/',views.manager_dashboard, name='manager_dashboard'),
]
