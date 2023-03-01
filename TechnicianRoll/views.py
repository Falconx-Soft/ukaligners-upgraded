from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Technician
from Case.models import Case, Case_additional_images, Case_additional_videos
# Create your views here.

@login_required(login_url='login')
def technician_dashboard(request):
    if request.user.is_technician:
        technician_obj = Technician.objects.get(user=request.user)
        case_list = Case.objects.filter(technician=technician_obj)
        context = {
            'case_list':case_list
        }
        return render(request,'technicianRoll/dashboard.html',context)
    return redirect('login')

@login_required(login_url='login')
def case_accepted(request, id):
    if request.user.is_technician:
        case_obj = Case.objects.get(id=id)
        additional_images_obj = Case_additional_images.objects.filter(case=case_obj)
        additional_videos_obj = Case_additional_videos.objects.filter(case=case_obj)
        if request.method == "POST":
            progress = request.POST.get("progress")
            case_obj.progress = progress
            if progress == "posted":
                case_obj.status = "treatment"
            case_obj.save()
            return redirect('TechnicianRoll:technician_dashboard')
        context = {
            'case_obj':case_obj,
            'additional_images_obj':additional_images_obj,
            'additional_videos_obj':additional_videos_obj,
        }
        return render(request,'technicianRoll/case_accepted.html',context)
    return redirect('login')