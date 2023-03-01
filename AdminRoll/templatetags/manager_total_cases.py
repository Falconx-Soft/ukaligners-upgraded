from django import template
from ..models import *
from Case.models import *
from SaloonRoll.models import *
register = template.Library()



def manager_total_cases(id):
    manager_obj = Manager.objects.get(id = id)
    dentist_obj = Dentist.objects.filter(manager = manager_obj)
    Saloon_owner_obj = Saloon_owner.objects.filter(manager = manager_obj)
    total_case = 0
    for dentist in dentist_obj:
        case_obj = Case.objects.filter(dentist = dentist)
        total_case = total_case + len(case_obj)
    for saloon in Saloon_owner_obj:
        case_obj = Case.objects.filter(saloon_owner = saloon)
        total_case = total_case + len(case_obj)
    print(total_case)
    return total_case

register.filter('manager_total_cases', manager_total_cases)