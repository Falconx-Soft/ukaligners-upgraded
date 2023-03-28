from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Case.models import Case
from .models import Clinic

@login_required(login_url='login')
# Create your views here.

def clinic_dashboard(request):
    clinic = Clinic.objects.get(user=request.user)
    case_list = Case.objects.filter(clinic=clinic)
    context = {
        'case_list':case_list
    }
    return render(request,'clinicRoll/dashboard.html',context)