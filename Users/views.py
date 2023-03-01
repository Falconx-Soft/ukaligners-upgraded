from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse, JsonResponse
from .models import Account as User
from .forms import CutomUserCreationForm
from django.conf import settings
from django.core.mail import send_mail
from DentistRoll.models import Dentist
# Create your views here.

def user_login(request):
    if request.user.is_authenticated:
        if request.user.is_admin:
            return redirect('AdminRoll:admin_dashboard') 
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = User.objects.get(email=email)
            user = authenticate(request, username=email, password=password) # check password

            if user:
                login(request, user)

                if user.is_admin:
                    return redirect('AdminRoll:admin_dashboard')
                elif user.is_dentist:
                    return redirect('DentistRoll:dentist_dashboard')
                elif user.is_salon:
                    return redirect('SaloonRoll:saloon_dashboard')
                elif user.is_manager:
                    return redirect('ManagerRoll:manager_dashboard')
                elif user.is_planner:
                    return redirect('PlannerRoll:planner_dashboard')
                elif user.is_technician:
                    return redirect('TechnicianRoll:technician_dashboard')
                else:
                    return HttpResponse('Roll does not recognized')
            else:
                context = {
                    'error_msg':"Password is incorrect"
                }
                return render(request,'users/login.html',context)
        except:
            context = {
                'error_msg':"User does not exist"
            }
            return render(request,'users/login.html',context)
    return render(request,'users/login.html')

def sign_up(request):
    context = {}
    form = CutomUserCreationForm
    if request.method == 'POST':
        form = CutomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()

            surname = request.POST.get('surname')
            number = request.POST.get('number')


            admin_obj_list = User.objects.filter(is_admin = True)
            admin_email_list = []
            for obj in admin_obj_list:
                admin_email_list.append(obj.email)

            user.is_dentist = True
            user.save()

            dentist_obj = Dentist.objects.create(user=user, surname=surname, number=number)
            dentist_obj.save()

            subject = 'New Dentist created'
            message = 'A new dentist is created'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = admin_email_list
            send_mail(subject, message, email_from, recipient_list)
            return redirect('login')
    
    context['form'] = form
    return render(request,'users/sign-up.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def home(request):

    return JsonResponse({'Status':200})
