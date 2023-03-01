from django import template
from ..models import *
from Case.models import *
from DentistRoll.models import Dentist
register = template.Library()



def saloon_case_accepted(id):
    saloon_owner_obj = Saloon_owner.objects.get(id = id)
    case_obj_accept = Case.objects.filter(saloon_owner = saloon_owner_obj , status = 'accepted')
    case_obj_tc = Case.objects.filter(saloon_owner = saloon_owner_obj , status = 'tc')
    case_obj_treatment = Case.objects.filter(saloon_owner = saloon_owner_obj , status = 'treatment')
    total = len(case_obj_accept) + len(case_obj_tc) + len(case_obj_treatment)
    print(total)
    return total

register.filter('saloon_case_accepted', saloon_case_accepted)