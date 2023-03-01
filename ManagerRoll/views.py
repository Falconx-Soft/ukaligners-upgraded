from django.shortcuts import render, redirect
from .models import Manager
from Case.models import Case
# Create your views here.

def manager_dashboard(request):
    if request.user.is_manager:
        manager_obj = Manager.objects.get(user=request.user)
        case_list = Case.objects.filter(dentist__manager=manager_obj)
        print(case_list)
        context = {
            'case_list':case_list
        }
        return render(request,'managerRoll/dashboard.html',context)
    return redirect('login')
