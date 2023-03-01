from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from Case.models import Case, Case_additional_images, Case_additional_videos
from .models import Planner
from django.conf import settings
from django.core.mail import send_mail
from Users.models import Account as User
# Create your views here.

@login_required(login_url='login')
def planner_dashboard(request):
    if request.user.is_planner:
        planner_obj = Planner.objects.get(user=request.user)
        print(planner_obj)
        case_list = Case.objects.filter(planner=planner_obj)
        print(case_list)
        context = {
            'case_list':case_list
        }
        return render(request,'plannerRoll/dashboard.html',context)
    return redirect('login')


@login_required(login_url='login')
def case_details(request,id):
    if request.user.is_planner:
        case_obj = Case.objects.get(id=id)
        additional_images_obj = Case_additional_images.objects.filter(case=case_obj)
        additional_videos_obj = Case_additional_videos.objects.filter(case=case_obj)
        if request.method == "POST":
            ortho_id = request.POST.get('ortho_id')
            aligner_upper = request.POST.get('aligner_upper')
            aligner_lower = request.POST.get('aligner_lower')
            retainer_upper = request.POST.get('retainer_upper')
            retainer_lower = request.POST.get('retainer_lower')
            treatment_plan_upper = request.POST.get('treatment_plan_upper')
            treatment_plan_lower = request.POST.get('treatment_plan_lower')
            duration = request.POST.get('duration')
            videos = request.FILES.getlist('videos')
            if ortho_id != '':
                case_obj.ortho_id = ortho_id
            if aligner_upper != '':
                case_obj.aligners_upper = aligner_upper
            if aligner_lower != '':
                case_obj.aligners_lower = aligner_lower
            if retainer_upper != '':
                case_obj.retainer_upper = retainer_upper
            if retainer_lower != '':
                case_obj.retainer_lower = retainer_lower
            if treatment_plan_upper != '':
                case_obj.treatment_plan_upper = treatment_plan_upper
            if treatment_plan_lower != '':
                case_obj.treatment_plan_lower = treatment_plan_lower
            if duration != '':
                case_obj.duration = duration
            case_obj.save()

            for video in videos:
                Case_additional_videos.objects.create(case = case_obj, video = video)

            case_obj.status = 'waiting acceptance'
            case_obj.save()

            admin_obj_list = User.objects.filter(is_admin = True)
            email_list = []
            for obj in admin_obj_list:
                email_list.append(obj.email)

            if case_obj.dentist:
                email_list.append(case_obj.dentist.user.email)
            else:
                email_list.append(case_obj.saloon_owner.user.email)

            subject = 'waiting acceptance'
            message = 'Planner update the case'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = email_list
            send_mail(subject, message, email_from, recipient_list)
            return redirect('PlannerRoll:planner_dashboard')
        context = {
            'case_obj':case_obj,
            'additional_images_obj':additional_images_obj,
            'additional_videos_obj':additional_videos_obj
        }
        return render(request,'plannerRoll/case_deatils.html',context)
    return redirect('login')
