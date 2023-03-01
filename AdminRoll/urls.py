from django.urls import path
from . import views
app_name = "AdminRoll"
urlpatterns = [
    path('dashboard/',views.admin_dashboard, name='admin_dashboard'),

    path('create-user/<str:user_type>/',views.create_user, name='create_user'),
    path('delete-user/<int:id>/<str:user_type>/' , views.delete_user, name="delete_user"),

    path('create-client/<str:user_type>/', views.create_client, name="create_client"),

    path('dentist-list/',views.dentist_list, name='dentist_list'),
    path('edit-dentist/<int:id>/',views.edit_dentist, name='edit_dentist'),
    path('delete-dentist/<int:id>/',views.delete_dentist, name='delete_dentist'),
    path('clinic-list/', views.clinic_list, name="clinic_list"),
    path('create-clinic/', views.create_clinic, name="create_clinic"),
    path('edit-clinic/<int:id>/', views.edit_clinic, name="edit_clinic"),
    path('delete-clinic/<int:id>/', views.delete_clinic, name="delete_clinic"),

    path('saloon-owner-list/',views.saloon_owner_list, name='saloon_owner_list'),
    path('edit-saloon/<int:id>/',views.edit_saloon_owner, name='edit_saloon_owner'),
    path('delete-saloon-owner/<int:id>/',views.delete_saloon_owner, name='delete_saloon_owner'),
    path('saloon-list/', views.saloon_list, name="saloon_list"),
    path('create-saloon/', views.create_saloon, name="create_saloon"),

    path('manager-list/',views.manager_list, name='manager_list'),
    path('edit-manager/<int:id>/',views.edit_manager, name='edit_manager'),

    path('planner-list/', views.planner_list, name="planner_list"),
    path('edit-planner/<int:id>/',views.edit_planner, name='edit_planner'),

    path('technician-list/', views.technician_list, name="technician_list"),
    path('edit-technician/<int:id>/', views.edit_technician, name="edit_technician"),

    path('add-case/',views.add_case_admin, name="add_case_admin"),

    path('case-details/<int:id>/', views.case_details, name="case_details"),

    path('case-accepted/<int:id>/', views.case_accepted, name="case_accepted"),

    path('view-details/<int:id>/', views.view_details, name="view_details"),

    path('case_treatment/<int:id>/', views.case_treatment, name="case_treatment"),

    path('complete-case/<int:id>/', views.complete_case, name="complete_case"),

    path('make-refinment/<int:id>/', views.make_refinment, name="make_refinment"),

    path('fee-list/', views.fee_list, name="fee_list"),
    path('fee-detail/<int:id>/', views.fee_detail, name="fee_detail"),
    path('expense/<int:id>/', views.expense, name="expense"),

    path('archive/<int:id>/', views.archive, name="archive"),

    path('case-fee/', views.case_fee, name="case_fee"),

]
