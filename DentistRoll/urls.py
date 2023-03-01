from django.urls import path
from . import views
app_name = "DentistRoll"
urlpatterns = [
    path('dashboard/',views.dentist_dashboard, name='dentist_dashboard'),
    path('edit-profile/',views.edit_profile, name="edit_profile"),
    path('add-case/', views.add_case, name="add_case"),
    path('edit-case/<int:id>/', views.edit_case, name="edit_case"),

    path('delete/<int:id>/', views.delete_additional_image, name="delete_additional_image"),

    path('waiting-case/<int:id>/', views.waiting_case_details, name="waiting_case_details"),
]
