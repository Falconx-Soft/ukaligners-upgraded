from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Saloon_owner, Saloon
from .forms import Saloon_ownerForm
from Case.models import Case, Case_additional_images, Case_additional_videos
from Case.forms import CaseForm
from Users.models import Account as User
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.

@login_required(login_url='login')
def saloon_dashboard(request):
    saloon_owner_obj = Saloon_owner.objects.get(user=request.user)
    case_list = Case.objects.filter(saloon_owner=saloon_owner_obj)
    context = {
        'case_list':case_list
    }
    return render(request,'SaloonRoll/dashboard.html',context)

@login_required(login_url='login')
def add_case(request):
    form = CaseForm
    saloon_owner_obj = Saloon_owner.objects.get(user=request.user)
    if request.method == "POST":
        form = CaseForm(request.POST, request.FILES)
        if form.is_valid():
            form_obj = form.save(commit=False)
            form_obj.saloon_owner = saloon_owner_obj
            saloon_id = request.POST.get('saloon_id')
            saloon_selected = Saloon.objects.get(id=saloon_id)
            form_obj.saloon = saloon_selected
            form_obj.save()
            images = request.FILES.getlist('additional_photos')
            for image in images:
                additional_image = Case_additional_images.objects.create(case=form_obj, image=image)
                additional_image.save()

            admin_obj_list = User.objects.filter(is_admin = True)
            admin_email_list = []
            for obj in admin_obj_list:
                admin_email_list.append(obj.email)
            subject = 'New case'
            message = 'A new case is created'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = admin_email_list
            send_mail(subject, message, email_from, recipient_list)
                
            return redirect('SaloonRoll:saloon_dashboard')
        else:
             print(form.errors.as_data())
    context = {
        'saloon_owner_obj':saloon_owner_obj,
        'form':form
    }
    return render(request,'saloonRoll/add_case.html',context)

@login_required(login_url='login')
def edit_case(request,id):
    case_obj = Case.objects.get(id=id)
    form = CaseForm(instance=case_obj)
    saloon_owner_obj = Saloon_owner.objects.get(user=request.user)
    additional_images_obj = Case_additional_images.objects.filter(case=case_obj)

    if request.method == "POST":
        form = CaseForm(request.POST,request.FILES, instance=case_obj)
        if form.is_valid():
            form_obj = form.save(commit=False)
            saloon_id = request.POST.get('saloon_id')
            saloon_selected = Saloon.objects.get(id=saloon_id)
            form_obj.saloon = saloon_selected
            form_obj.saloon_owner = saloon_owner_obj
            form_obj.save()
            images = request.FILES.getlist('additional_photos')
            for image in images:
                additional_image = Case_additional_images.objects.create(case=form_obj, image=image)
                additional_image.save()
            return redirect('SaloonRoll:saloon_dashboard')
        else:
             print(form.errors.as_data(),"<-----------")

    context = {
        'case_obj':case_obj,
        'form':form,
        'saloon_owner_obj':saloon_owner_obj,
        'additional_images_obj':additional_images_obj
    }
    return render(request,'saloonRoll/edit_case.html', context)

@login_required(login_url='login')
def edit_profile(request):
    if request.user.is_salon:
        saloon_owner_obj = Saloon_owner.objects.get(user=request.user)
        form = Saloon_ownerForm(instance=saloon_owner_obj)
        if request.method == "POST":
            form = Saloon_ownerForm(request.POST, instance=saloon_owner_obj)
            if form.is_valid():
                form.save()
                return redirect('SaloonRoll:saloon_dashboard')
        context = {
            'saloon_owner_obj':saloon_owner_obj,
            'form':form
        }
        return render(request,'saloonRoll/saloon_owner_edit.html',context)
    else:
        return redirect('login')

@login_required(login_url='login')
def waiting_case_details(request,id):
    if request.user.is_admin or request.user.is_salon:
        case_obj = Case.objects.get(id=id)
        additional_images_obj = Case_additional_images.objects.filter(case=case_obj)
        additional_videos_obj = Case_additional_videos.objects.filter(case=case_obj)
        if request.method == "POST":
            treatment_type = request.POST.get("treatment_type")
            status = request.POST.get("status")
            case_obj.treatment_type = treatment_type
            case_obj.status = status
            case_obj.save()
            if request.user.is_admin:
                return redirect('AdminRoll:admin_dashboard')
            else:
                admin_obj_list = User.objects.filter(is_admin = True)
                email_list = []
                for obj in admin_obj_list:
                    email_list.append(obj.email)
                subject = 'waiting acceptance'
                message = 'Planner update the case'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = email_list
                send_mail(subject, message, email_from, recipient_list)

                return redirect('SaloonRoll:saloon_dashboard')
        context = {
            'case_obj':case_obj,
            'additional_images_obj':additional_images_obj,
            'additional_videos_obj':additional_videos_obj
        }
        return render(request,'dentistRoll/waiting_case_details.html',context)
    else:
        return redirect('login')