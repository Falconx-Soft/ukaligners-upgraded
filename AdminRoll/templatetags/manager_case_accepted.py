from django import template
from ..models import *
from Case.models import *
from SaloonRoll.models import *
register = template.Library()



def manager_case_accepted(id):
    manager_obj = Manager.objects.get(id = id)
    dentist_obj = Dentist.objects.filter(manager = manager_obj)
    Saloon_owner_obj = Saloon_owner.objects.filter(manager = manager_obj)
    total_case = 0
    for dentist in dentist_obj:
        case_obj_accept = Case.objects.filter(dentist = dentist, status = 'accepted')
        case_obj_tc = Case.objects.filter(dentist = dentist, status = 'tc')
        case_obj_treatment = Case.objects.filter(dentist = dentist, status = 'treatment')
        total_case = total_case + len(case_obj_accept)
        total_case = total_case + len(case_obj_tc)
        total_case = total_case + len(case_obj_treatment)
    for saloon in Saloon_owner_obj:
        case_obj_accept = Case.objects.filter(saloon_owner = saloon, status = 'accepted')
        case_obj_tc = Case.objects.filter(saloon_owner = saloon, status = 'tc')
        case_obj_treatment = Case.objects.filter(saloon_owner = saloon, status = 'treatment')
        total_case = total_case + len(case_obj_accept)
        total_case = total_case + len(case_obj_tc)
        total_case = total_case + len(case_obj_treatment)
    return total_case

register.filter('manager_case_accepted', manager_case_accepted)