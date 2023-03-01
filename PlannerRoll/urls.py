from django.urls import path
from . import views
app_name = "PlannerRoll"
urlpatterns = [
    path('dashboard/',views.planner_dashboard, name='planner_dashboard'),
    path('case-details/<int:id>/', views.case_details, name="case_details"),
]
