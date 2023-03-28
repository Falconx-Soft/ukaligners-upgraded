from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from Users.models import Account as Users

from .models import fee

from DentistRoll.models import Dentist, Clinic
from DentistRoll.forms import DentistForm, ClinicForm

from SaloonRoll.models import Saloon_owner, Saloon
from SaloonRoll.forms import Saloon_ownerForm, SaloonForm

from ManagerRoll.models import Manager
from ManagerRoll.forms import ManagerForm

from PlannerRoll.models import Planner
from PlannerRoll.form import PlannerForm

from TechnicianRoll.models import Technician
from TechnicianRoll.forms import TechnicianForm

from Case.models import Case, Case_additional_images, Case_additional_videos
from Case.forms import CaseForm

from Users.forms import CutomUserCreationForm
from django.conf import settings
from django.core.mail import send_mail

from itertools import chain
# Create your views here. 

###################################################### Dashboard
@login_required(login_url='login')
def admin_dashboard(request):
    if request.user.is_admin:
        case_list = Case.objects.all().order_by('-id')
        context = {
            'case_list':case_list
        }
        return render(request,'adminRoll/dashboard.html',context)
    return redirect('login')

###################################################### User

@login_required(login_url='login')
def create_user(request,user_type):
    if request.user.is_admin:
        form = CutomUserCreationForm
        if request.method == 'POST':
            form = CutomUserCreationForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.username = user.username.lower()

                if user_type == "manager":
                    user.is_manager = True
                    user.save()
                    number = request.POST.get('number')
                    fee = request.POST.get('fee')
                    manager_obj = Manager.objects.create(user=user, number=number, fee=fee)
                    manager_obj.save()
                    return redirect('AdminRoll:manager_list')
                elif user_type == "planner":
                    user.is_planner = True
                    user.save()
                    number = request.POST.get('number')
                    fee = request.POST.get('fee')
                    planner_obj = Planner.objects.create(user=user, number=number, fee=fee)
                    planner_obj.save()
                    return redirect('AdminRoll:planner_list')
                elif user_type == "technician":
                    user.is_technician = True
                    user.save()
                    number = request.POST.get('number')
                    fee = request.POST.get('fee')
                    technician_obj = Technician.objects.create(user=user, number=number, fee=fee)
                    technician_obj.save()
                    return redirect('AdminRoll:technician_list')
                    

        context = {
            'user_type':user_type,
            'form':form
        }
        return render(request,'adminRoll/create_users.html',context)
    return redirect('login')

@login_required(login_url='login')
def delete_user(request,id,user_type):
    if request.user.is_admin:
        if user_type == "manager":
            manager_obj = Manager.objects.get(id=id)
            user_obj = manager_obj.user
            user_obj.is_active = False
            user_obj.save()
            return redirect('AdminRoll:manager_list')
        elif user_type == "planner":
            planner_obj = Planner.objects.get(id=id)
            user_obj = planner_obj.user
            user_obj.is_active = False
            user_obj.save()
            return redirect('AdminRoll:planner_list')
        elif user_type == "technician":
            technician_obj = Technician.objects.get(id=id)
            user_obj = technician_obj.user
            user_obj.is_active = False
            user_obj.save()
            return redirect('AdminRoll:technician_list')
    return redirect('login')

###################################################### Create Client

@login_required(login_url='login')
def create_client(request,user_type):
    if request.user.is_admin:
        form = CutomUserCreationForm
        if request.method == 'POST':
            form = CutomUserCreationForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.username = user.username.lower()

                if user_type == "dentist":
                    user.is_dentist = True
                    user.save()
                    number = request.POST.get('number')
                    surname = request.POST.get('surname')
                    dentist_obj = Dentist.objects.create(user=user, number=number, surname=surname)
                    dentist_obj.save()
                    return redirect('AdminRoll:dentist_list')
                elif user_type == "saloon":
                    user.is_salon = True
                    user.save()
                    number = request.POST.get('number')
                    surname = request.POST.get('surname')
                    saloon_owner_obj = Saloon_owner.objects.create(user=user, number=number, surname=surname)
                    saloon_owner_obj.save()
                    return redirect('AdminRoll:saloon_owner_list')
        context = {
            'user_type':user_type,
            'form':form
        }
        return render(request,'adminRoll/create_client.html',context)
    return redirect('login')

###################################################### Dentist

@login_required(login_url='login')
def dentist_list(request):
    if request.user.is_admin:
        dentist_obj_list = Dentist.objects.filter(user__is_active = True)
        context = {
            'dentist_obj_list':dentist_obj_list
        }
        return render(request,'adminRoll/dentist_list.html',context)
    return redirect('login')

@login_required(login_url='login')
def edit_dentist(request,id):
    if request.user.is_admin:
        dentist_obj = Dentist.objects.get(id=id)
        form = DentistForm(instance=dentist_obj)
        if request.method == "POST":
            form = DentistForm(request.POST, instance=dentist_obj)
            if form.is_valid():
                dentist_update = form.save(commit=False)
                dentist_update.save()
                form.save_m2m()
                return redirect('AdminRoll:dentist_list')
        context = {
            'dentist_obj':dentist_obj,
            'form':form
        }
        return render(request,'adminRoll/dentist_edit.html',context)
    else:
        return redirect('login')

@login_required(login_url='login')
def delete_dentist(request,id):
    if request.user.is_admin:
        dentist_obj = Dentist.objects.get(id=id)
        user_obj = dentist_obj.user
        user_obj.is_active = False
        user_obj.save()
        return redirect('AdminRoll:dentist_list')
    else:
        return redirect('login')

############################# Clinic

@login_required(login_url='login')
def clinic_list(request):
    if request.user.is_admin:
        clinic_list_obj = Clinic.objects.all()
        context = {
            'clinic_list_obj':clinic_list_obj
        }
        return render(request,'adminRoll/clinic_list.html',context)
    else:
        return redirect('login')

@login_required(login_url='login')
def create_clinic(request):
    if request.user.is_admin == True or request.user.is_dentist == True:
        form = ClinicForm
        if request.method == "POST":
            form = ClinicForm(request.POST)
            if form.is_valid():
                new_clinic = form.save(commit=False)
                new_clinic.save()
                if request.user.is_admin:
                    return redirect('AdminRoll:clinic_list')
                else:
                    return redirect('DentistRoll:dentist_dashboard')
        context = {
            'form':form,
            'type':'Clinic',
        }
        return render(request,'adminRoll/create_clinic.html',context)
    else:
        return redirect('login')

@login_required(login_url='login')
def edit_clinic(request,id):
    if request.user.is_admin == True:
        clinic_obj = Clinic.objects.get(id=id)
        form = ClinicForm(instance=clinic_obj)
        if request.method == "POST":
            form = ClinicForm(request.POST, instance=clinic_obj)
            if form.is_valid():
                form.save()
                return redirect('AdminRoll:clinic_list')
        context = {
            'form':form,
            'clinic_obj':clinic_obj,
            'type':'Clinic',
        }
        return render(request,'adminRoll/create_clinic.html',context)
    else:
        return redirect('login')

@login_required(login_url='login')
def delete_clinic(request,id):
    if request.user.is_admin == True:
        clinic_obj = Clinic.objects.get(id=id)
        clinic_obj.delete()
        return redirect('AdminRoll:clinic_list')
    else:
        return redirect('login')    

###################################################### Saloon Owner

@login_required(login_url='login')
def saloon_owner_list(request):
    if request.user.is_admin:
        saloon_owner_list = Saloon_owner.objects.all()
        context = {
            'saloon_owner_list':saloon_owner_list
        }
        return render(request,'adminRoll/saloon_owner_list.html',context)
    return redirect('login')

@login_required(login_url='login')
def edit_saloon_owner(request,id):
    if request.user.is_admin:
        saloon_owner_obj = Saloon_owner.objects.get(id=id)
        form = Saloon_ownerForm(instance=saloon_owner_obj)
        if request.method == "POST":
            form = Saloon_ownerForm(request.POST, instance=saloon_owner_obj)
            if form.is_valid():
                dentist_update = form.save(commit=False)
                dentist_update.save()
                form.save_m2m()
                return redirect('AdminRoll:saloon_owner_list')
        context = {
            'saloon_owner_obj':saloon_owner_obj,
            'form':form
        }
        return render(request,'adminRoll/saloon_owner_edit.html',context)
    else:
        return redirect('login')

@login_required(login_url='login')
def delete_saloon_owner(request,id):
    if request.user.is_admin:
        saloon_owner_obj = Saloon_owner.objects.get(id=id)

        cases_obj = Case.objects.filter(saloon_owner = saloon_owner_obj)

        for obj in cases_obj:
            obj.saloon_owner = None
            obj.save()

        saloon_owner_obj.user.delete()
        return redirect('AdminRoll:saloon_owner_list')
    else:
        return redirect('login')

############################# Saloon

@login_required(login_url='login')
def saloon_list(request):
    if request.user.is_admin:
        saloon_list_obj = Saloon.objects.all()
        context = {
            'saloon_list_obj':saloon_list_obj
        }
        return render(request,'adminRoll/saloon_list.html',context)
    else:
        return redirect('login')


@login_required(login_url='login')
def create_saloon(request):
    if request.user.is_admin or request.user.is_salon:
        form = SaloonForm
        if request.method == "POST":
            form = SaloonForm(request.POST)
            if form.is_valid():
                form.save()
                if request.user.is_salon:
                    return redirect('SaloonRoll:saloon_dashboard')
                return redirect('AdminRoll:saloon_list')
        context = {
            'form':form,
            'type':'Saloon',
        }
        return render(request,'adminRoll/create_clinic.html',context)
    else:
        return redirect('login')

###################################################### Manager

@login_required(login_url='login')
def manager_list(request):
    if request.user.is_admin:
        manager_obj_list = Manager.objects.filter(user__is_active = True)
        context = {
            'manager_obj_list':manager_obj_list
        }
        return render(request,'adminRoll/manager_list.html',context)
    else:
        return redirect('login')

@login_required(login_url='login')
def edit_manager(request,id):
    if request.user.is_admin:
        manager_obj = Manager.objects.get(id=id)
        form = ManagerForm(instance=manager_obj)
        if request.method == "POST":
            form = ManagerForm(request.POST, instance=manager_obj)
            if form.is_valid():
                form.save()
                return redirect('AdminRoll:manager_list')
        context = {
            'manager_obj':manager_obj,
            'form':form
        }
        return render(request,'adminRoll/manager_edit.html',context)
    else:
        return redirect('login')

###################################################### Manager

@login_required(login_url='login')
def planner_list(request):
    if request.user.is_admin:
        planner_obj_list = Planner.objects.filter(user__is_active = True)
        context = {
            'planner_obj_list':planner_obj_list
        }
        return render(request,'adminRoll/planner_list.html',context)
    else:
        return redirect('login')

@login_required(login_url='login')
def edit_planner(request,id):
    if request.user.is_admin:
        planner_obj = Planner.objects.get(id=id)
        form = PlannerForm(instance=planner_obj)
        if request.method == "POST":
            form = PlannerForm(request.POST, instance=planner_obj)
            if form.is_valid():
                form.save()
                return redirect('AdminRoll:planner_list')
        context = {
            'planner_obj':planner_obj,
            'form':form
        }
        return render(request,'adminRoll/planner_edit.html',context)
    else:
        return redirect('login')

###################################################### Manager

@login_required(login_url='login')
def technician_list(request):
    if request.user.is_admin:
        technician_obj_list = Technician.objects.filter(user__is_active = True)
        context = {
            'technician_obj_list':technician_obj_list
        }
        return render(request,'adminRoll/technician_list.html',context)
    else:
        return redirect('login')

@login_required(login_url='login')
def edit_technician(request,id):
    if request.user.is_admin:
        technician_obj = Technician.objects.get(id=id)
        form = TechnicianForm(instance=technician_obj)
        if request.method == "POST":
            form = TechnicianForm(request.POST, instance=technician_obj)
            if form.is_valid():
                form.save()
                return redirect('AdminRoll:technician_list')
        context = {
            'technician_obj':technician_obj,
            'form':form
        }
        return render(request,'adminRoll/technician_edit.html',context)
    else:
        return redirect('login')

##################################################### Case

@login_required(login_url='login')
def add_case_admin(request):
    if request.user.is_admin:
        form = CaseForm
        dentist_list = Dentist.objects.all()
        clinic_list = Clinic.objects.all()
        if request.method == "POST":
            form = CaseForm(request.POST, request.FILES)
            if form.is_valid():
                form_obj = form.save(commit=False)
                
                clinic_id = request.POST.get('clinic_id')
                clinic_obj = Clinic.objects.get(id=clinic_id)

                dentist_id = request.POST.get('dentist_id')
                dentist_obj = Dentist.objects.get(id=dentist_id)

                form_obj.clinic = clinic_obj
                form_obj.dentist = dentist_obj

                form_obj.save()
                images = request.FILES.getlist('additional_photos')
                for image in images:
                    additional_image = Case_additional_images.objects.create(case=form_obj, image=image)
                    additional_image.save()
                    
                return redirect('AdminRoll:admin_dashboard')
            else:
                print(form.errors.as_data())
        context = {
            'form':form,
            'dentist_list':dentist_list,
            'clinic_list':clinic_list
        }
        return render(request,'adminRoll/add_case.html',context)
    else:
        return redirect('login')

@login_required(login_url='login')
def case_details(request,id):
    if request.user.is_admin:
        case_obj = Case.objects.get(id=id)
        additional_images_obj = Case_additional_images.objects.filter(case=case_obj)
        planner_obj = Planner.objects.all()
        if request.method == "POST":
            planner_id = request.POST.get("planner")
            planner_selected = Planner.objects.get(id=planner_id)
            case_obj.planner = planner_selected
            case_obj.save()
            subject = 'New case'
            message = 'A new case is assigned to you'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [planner_selected.user.email]
            send_mail(subject, message, email_from, recipient_list)
            return redirect('AdminRoll:admin_dashboard')
        context = {
            'case_obj':case_obj,
            'additional_images_obj':additional_images_obj,
            'planner':planner_obj,
        }
        return render(request,'adminRoll/case_deatils.html',context)
    else:
        return redirect('login')

@login_required(login_url='login')
def case_accepted(request,id):
    if request.user.is_admin:
        case_obj = Case.objects.get(id=id)
        additional_images_obj = Case_additional_images.objects.filter(case=case_obj)
        additional_videos_obj = Case_additional_videos.objects.filter(case=case_obj)
        technician_obj = Technician.objects.all()
        if request.method == "POST":
            status = request.POST.get("status")
            technician_id = request.POST.get("technician_id")
            case_obj.status = status

            try:
                technician_selected = Technician.objects.get(id=technician_id)
                case_obj.technician = technician_selected
                case_obj.progress = "on"
                
                subject = 'New case'
                message = 'A new case is assigned to you'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [technician_selected.user.email,]
                send_mail(subject, message, email_from, recipient_list)

                case_obj.save()
            except Exception as e:
                case_obj.save()
            return redirect('AdminRoll:admin_dashboard')
        context = {
            'case_obj':case_obj,
            'additional_images_obj':additional_images_obj,
            'additional_videos_obj':additional_videos_obj,
            'technician_obj':technician_obj
        }
        return render(request,'adminRoll/case_accepted.html',context)
    else:
        return redirect('login')

@login_required(login_url='login')
def view_details(request,id):
    case_obj = Case.objects.get(id=id)
    additional_images_obj = Case_additional_images.objects.filter(case=case_obj)
    additional_videos_obj = Case_additional_videos.objects.filter(case=case_obj)

    context = {
        'case_obj':case_obj,
        'additional_images_obj':additional_images_obj,
        'additional_videos_obj':additional_videos_obj,
    }
    return render(request,'adminRoll/view_details.html',context)

@login_required(login_url='login')
def case_treatment(request,id):
    case_obj = Case.objects.get(id=id)
    additional_images_obj = Case_additional_images.objects.filter(case=case_obj)
    additional_videos_obj = Case_additional_videos.objects.filter(case=case_obj)

    context = {
        'case_obj':case_obj,
        'additional_images_obj':additional_images_obj,
        'additional_videos_obj':additional_videos_obj,
    }
    return render(request,'adminRoll/case_treatment.html',context)

@login_required(login_url='login')
def complete_case(request,id):
    case_obj = Case.objects.get(id=id)
    case_obj.status = "tc"
    case_obj.save()
    if request.user.is_admin:
        return redirect('AdminRoll:admin_dashboard')
    elif request.user.is_dentist:
        return redirect('DentistRoll:dentist_dashboard')
    elif request.user.is_salon:
        return redirect('SaloonRoll:saloon_dashboard')

@login_required(login_url='login')
def make_refinment(request,id):
    case_obj = Case.objects.get(id=id)

    if case_obj.dentist:
        new_case = Case.objects.create(
                    clinic =  case_obj.clinic,
                    dentist = case_obj.dentist,
                    name = case_obj.name,
                    surname = case_obj.surname,
                    treatment_required = case_obj.treatment_required,
                    section = case_obj.section,
                    refinement = case_obj.refinement + 1,
                    )
        new_case.save()
    else:
        new_case = Case.objects.create(
                    saloon =  case_obj.saloon,
                    saloon_owner = case_obj.saloon_owner,
                    name = case_obj.name,
                    surname = case_obj.surname,
                    treatment_required = case_obj.treatment_required,
                    section = case_obj.section,
                    refinement = case_obj.refinement + 1,
                    )
        new_case.save()
    if request.user.is_admin:
        return redirect('AdminRoll:admin_dashboard')
    elif request.user.is_dentist:
        return redirect('DentistRoll:dentist_dashboard')
    elif request.user.is_salon:
        return redirect('SaloonRoll:saloon_dashboard')

@login_required(login_url='login')
def fee_list(request):
    if request.user.is_admin:

        cases_accept = Case.objects.filter(status = 'accepted', fee_cleared=False)
        cases_tc = Case.objects.filter(status = 'tc', fee_cleared=False)
        cases_treatment = Case.objects.filter(status = 'treatment', fee_cleared=False)

        total_unpaid_cases = list(chain(cases_accept, cases_tc, cases_treatment))


        cases_accept_paid = Case.objects.filter(status = 'accepted', fee_cleared=True)
        cases_tc_paid = Case.objects.filter(status = 'tc', fee_cleared=True)
        cases_treatment_paid = Case.objects.filter(status = 'treatment', fee_cleared=True)

        total_paid_cases = list(chain(cases_accept_paid, cases_tc_paid, cases_treatment_paid))

        context = {
            'total_unpaid_cases':total_unpaid_cases,
            'total_paid_cases':total_paid_cases
        }
    
        return render(request,'adminRoll/fee.html',context)
    else:
        return redirect('login')

@login_required(login_url='login')
def fee_detail(request,id):
    if request.user.is_admin:
        cases_obj = Case.objects.get(id = id)
        total_plan = cases_obj.treatment_plan_upper + cases_obj.treatment_plan_lower
        total_aligners = cases_obj.aligners_upper + cases_obj.aligners_lower
        total_retainer = cases_obj.retainer_upper + cases_obj.retainer_lower
        monitring = 0
        if cases_obj.treatment_type != "essential":
            monitring = cases_obj.duration
        total_amount = (total_plan*40) + (total_aligners*25) + (total_retainer * 30) + (monitring * 5)
        context = {
            'total_plan':total_plan,
            'total_aligners':total_aligners,
            'total_retainer':total_retainer,
            'monitring':monitring,
            'total_amount':total_amount
        }
        return render(request,'adminRoll/fee_details.html',context)
    else:
        return redirect('login')

@login_required(login_url='login')
def expense(request,id):
    if request.user.is_admin:
        cases_obj = Case.objects.get(id = id)
        total_plan = cases_obj.treatment_plan_upper + cases_obj.treatment_plan_lower
        total_aligners = cases_obj.aligners_upper + cases_obj.aligners_lower
        
        total_amount = cases_obj.totel_fee

        manager_fee = 0
        if cases_obj.dentist:
            try:
                manager_fee = cases_obj.dentist.manager.fee
            except:
                pass
        else:
            manager_fee = cases_obj.saloon_owner.manager.fee
        percentage = (float(manager_fee)/100)*float(total_amount)

        technician_fee =  0
        if cases_obj.technician:
            technician_fee = cases_obj.technician.fee

        planner_fee = 0
        if cases_obj.planner:
            planner_fee = cases_obj.planner.fee

        total_expense = percentage + (technician_fee * total_aligners) + (total_plan * planner_fee)

        if request.method == "POST":
            if request.POST.get('manager_paid') == 'paid':
                cases_obj.manager_paid = True
            else:
                cases_obj.manager_paid = False

            if request.POST.get('planner_paid') == 'paid':
                cases_obj.planner_paid = True
            else:
                cases_obj.planner_paid = False
                
            if request.POST.get('technician_paid') == 'paid':
                cases_obj.technician_paid = True
            else:
                cases_obj.technician_paid = False

            cases_obj.save()


        context = {
            'total_amount':total_amount,
            'manager_fee':manager_fee,
            'percentage':round(percentage, 2),
            'technician_fee':technician_fee,
            'total_aligners':total_aligners,
            'total_plan':total_plan,
            'planner_fee':planner_fee,
            'total_expense':round(total_expense, 2),
            'cases_obj':cases_obj

        }
        return render(request,'adminRoll/expense.html',context)
    else:
        return redirect('login')
    
@login_required(login_url='login')
def archive(request,id):
    if request.user.is_admin:
        case_obj = Case.objects.get(id=id)
        case_obj.fee_cleared = True
        case_obj.save()
        return redirect('AdminRoll:fee_list')
    else:
        return redirect('login')

@login_required(login_url='login')
def case_fee(request):
    if request.user.is_admin:
        fee_obj_list = fee.objects.all()
        if fee_obj_list:
            fee_obj = fee_obj_list[0]
        else:
            fee_obj = None
        context = {
            'fee_obj':fee_obj
        }
        if request.method == "POST":
            if fee_obj_list:
                fee_obj.fee_plan = request.POST.get('fee_plan')
                fee_obj.fee_retainer = request.POST.get('fee_retainer')
                fee_obj.fee_aligner = request.POST.get('fee_aligner')
                fee_obj.fee_monitring = request.POST.get('fee_monitring')
                fee_obj.fee_comprehensive = request.POST.get('fee_comprehensive')
                fee_obj.fee_replacement = request.POST.get('fee_replacement')
                fee_obj.fee_mouthguard = request.POST.get('fee_mouthguard')
                fee_obj.fee_smile_design = request.POST.get('fee_smile_design')
                fee_obj.save()
            else:
                temp = fee.objects.create(
                    fee_plan=request.POST.get('fee_plan'),
                    fee_retainer=request.POST.get('fee_retainer'),
                    fee_aligner=request.POST.get('fee_aligner'),
                    fee_monitring=request.POST.get('fee_monitring'),
                    fee_comprehensive=request.POST.get('fee_comprehensive'),
                    fee_replacement = request.POST.get('fee_replacement'),
                    fee_mouthguard = request.POST.get('fee_mouthguard'),
                    fee_smile_design = request.POST.get('fee_smile_design')
                )
                temp.save()
            return redirect('AdminRoll:admin_dashboard')
        return render(request,'adminRoll/case_fee.html',context)
    else:
        return redirect('login')