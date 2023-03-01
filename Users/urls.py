from django.urls import path
from . import views
urlpatterns = [
    path('',views.user_login, name='login'),
    path('sign-up/',views.sign_up, name='sign_up'),
    path('logout/', views.logoutUser, name='logout'),
    path('accounts/login/',views.user_login, name='login'),
    path('home/',views.home, name='home'),
]
