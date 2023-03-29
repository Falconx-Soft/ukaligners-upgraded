from django.shortcuts import render, redirect
from Case.forms import CaseForm
from Case.models import Case, Case_additional_images, Case_additional_videos
from django.contrib.auth.decorators import login_required
from .forms import DentistForm
from .models import *
from AdminRoll.models import fee
from PlannerRoll.models import Planner
from Users.models import Account as User
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.

@login_required(login_url='login')
def dentist_dashboard(request):
    dentist_obj = Dentist.objects.get(user=request.user)
    case_list = Case.objects.filter(dentist=dentist_obj).order_by('-id')
    print(case_list)
    context = {
        'case_list':case_list
    }
    return render(request,'dentistRoll/dashboard.html',context)

@login_required(login_url='login')
def edit_profile(request):
    if request.user.is_dentist:
        dentist_obj = Dentist.objects.get(user=request.user)
        form = DentistForm(instance=dentist_obj)
        if request.method == "POST":
            form = DentistForm(request.POST, instance=dentist_obj)
            if form.is_valid():
                form.save()
                return redirect('DentistRoll:dentist_dashboard')
        context = {
            'dentist_obj':dentist_obj,
            'form':form
        }
        return render(request,'dentistRoll/dentist_edit.html',context)
    else:
        return redirect('login')

@login_required(login_url='login')
def add_case(request):
    if request.user.is_admin or request.user.is_dentist:
        form = CaseForm
        dentist_obj = Dentist.objects.get(user=request.user)
        if request.method == "POST":
            form = CaseForm(request.POST, request.FILES)
            if form.is_valid():
                form_obj = form.save(commit=False)
                form_obj.dentist = dentist_obj
                clinic_id = request.POST.get('clinic_id')
                clinic_obj = Clinic.objects.get(id=clinic_id)
                form_obj.clinic = clinic_obj
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
                    
                return redirect('DentistRoll:dentist_dashboard')
            else:
                print(form.errors.as_data())
        context = {
            'dentist_obj':dentist_obj,
            'form':form
        }
        return render(request,'dentistRoll/add_case.html',context)
    else:
        return redirect('login')

@login_required(login_url='login')
def edit_case(request, id):
    if request.user.is_admin or request.user.is_dentist:
        context = {}
        case_obj = Case.objects.get(id=id)
        form = CaseForm(instance=case_obj)
        if request.user.is_admin:
            dentist_obj = Dentist.objects.all()
            clinic_list = Clinic.objects.all()
            planner_list = Planner.objects.all()
            context['clinic_list'] = clinic_list
            context['planner_list'] = planner_list
        else:
            dentist_obj = Dentist.objects.get(user=request.user)
            planner_obj = case_obj.planner
        additional_images_obj = Case_additional_images.objects.filter(case=case_obj)

        if request.method == "POST":
            form = CaseForm(request.POST,request.FILES, instance=case_obj)
            if form.is_valid():
                form_obj = form.save(commit=False)
                clinic_id = request.POST.get('clinic_id')
                clinic_obj = Clinic.objects.get(id=clinic_id)
                form_obj.clinic = clinic_obj
                if request.user.is_dentist:
                    form_obj.dentist = dentist_obj
                    form_obj.planner = planner_obj
                else:
                    dentist_id = request.POST.get('dentist_id')
                    dentist_obj = Dentist.objects.get(id=dentist_id)
                    form_obj.dentist = dentist_obj

                    planner_id = request.POST.get('planner_id')
                    planner_obj = Planner.objects.get(id=planner_id)
                    form_obj.planner = planner_obj
                form_obj.save()
                images = request.FILES.getlist('additional_photos')
                for image in images:
                    additional_image = Case_additional_images.objects.create(case=form_obj, image=image)
                    additional_image.save()
                if request.user.is_dentist: 
                    return redirect('DentistRoll:dentist_dashboard')
                else:
                    return redirect('AdminRoll:admin_dashboard')
            else:
                print(form.errors.as_data(),"<-----------")
                context['error_msg'] = 'Data is not valid.'

        context['case_obj'] = case_obj
        context['form'] = form
        context['dentist_obj'] = dentist_obj
        context['additional_images_obj'] = additional_images_obj
        return render(request,'dentistRoll/edit_case.html', context)
    else:
        return redirect('login')

@login_required(login_url='login')
def delete_additional_image(request, id):
    additional_image_obj = Case_additional_images.objects.get(id=id)
    case_id = additional_image_obj.case.id
    additional_image_obj.delete()
    return redirect('DentistRoll:edit_case', id=case_id)

@login_required(login_url='login')
def waiting_case_details(request, id):
    if request.user.is_admin or request.user.is_dentist:
        case_obj = Case.objects.get(id=id)
        additional_images_obj = Case_additional_images.objects.filter(case=case_obj)
        additional_videos_obj = Case_additional_videos.objects.filter(case=case_obj)

        total_plan = case_obj.treatment_plan_upper + case_obj.treatment_plan_lower
        total_aligners = case_obj.aligners_upper + case_obj.aligners_lower
        total_retainer = case_obj.retainer_upper + case_obj.retainer_lower

        case_fee_list = fee.objects.all()

        if case_fee_list:
            case_fee_obj = case_fee_list[0]
            fee_plan = case_fee_obj.fee_plan
            fee_retainer = case_fee_obj.fee_retainer
            fee_aligner = case_fee_obj.fee_aligner
            fee_monitring = case_fee_obj.fee_monitring
            fee_comprehensive = case_fee_obj.fee_comprehensive
            fee_replacement = case_fee_obj.fee_replacement
            fee_mouthguard = case_fee_obj.fee_mouthguard
            fee_smile_design = case_fee_obj.fee_smile_design
        else:
            fee_plan = 0
            fee_retainer = 0
            fee_aligner = 0
            fee_monitring = 0
            fee_comprehensive = 0

        monitring = 0
        
        total_amount_essential = (total_plan*fee_plan) + (total_aligners*fee_aligner) + (total_retainer * fee_retainer)   

        total_amount_advance = (case_obj.duration * fee_monitring)  

        total_amount_comprehensive = total_amount_advance + (total_aligners*fee_comprehensive)

        if case_obj.optional_treatment == "replacement":
            total_amount_essential += fee_replacement
        if case_obj.optional_treatment == "mouthguard":
            total_amount_essential += fee_mouthguard
        if case_obj.optional_treatment == "smile design":
            total_amount_essential += fee_smile_design

        if request.method == "POST":
            treatment_type = request.POST.get("treatment_type")
            status = request.POST.get("status")
            print(status,"<------------------")
            case_obj.treatment_type = treatment_type
            case_obj.status = status
            if status == "accepted":
                print("**************")
                if treatment_type == "essential":
                    total_amount = total_amount_essential
                    case_obj.totel_fee = total_amount - ((total_amount/100)*case_obj.dentist.discount)
                    print(total_amount,case_obj.dentist.discount,total_amount - ((total_amount/100)*case_obj.dentist.discount),"-------")
                elif treatment_type == "advance":
                    total_amount = total_amount_essential + total_amount_advance
                    case_obj.totel_fee = total_amount - ((total_amount/100)*case_obj.dentist.discount)
                    print(total_amount,case_obj.dentist.discount,total_amount - ((total_amount/100)*case_obj.dentist.discount),"********")
                else:
                    total_amount = total_amount_essential + total_amount_advance + total_amount_comprehensive
                    case_obj.totel_fee = total_amount - ((total_amount/100)*case_obj.dentist.discount)
                    print(total_amount,case_obj.dentist.discount,total_amount - ((total_amount/100)*case_obj.dentist.discount),"<<<<<<<<<<")
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

                return redirect('DentistRoll:dentist_dashboard')
        
        context = {
            'case_obj':case_obj,
            'additional_images_obj':additional_images_obj,
            'additional_videos_obj':additional_videos_obj,
            'total_amount_essential':total_amount_essential,
            'total_amount_advance':total_amount_advance,
            'total_amount_comprehensive':total_amount_comprehensive,
            'fee_plan':fee_plan,
            'total_plan':total_plan,
            'fee_retainer':fee_retainer,
            'total_retainer':total_retainer,
            'fee_aligner':fee_aligner,
            'total_aligners':total_aligners,
            'fee_monitring':fee_monitring,
            'monitring':case_obj.duration,
            'fee_comprehensive':fee_comprehensive
        }
        return render(request,'dentistRoll/waiting_case_details.html',context)
    else:
        return redirect('login')