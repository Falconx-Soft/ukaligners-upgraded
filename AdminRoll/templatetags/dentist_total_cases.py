from django import template
from ..models import *
from Case.models import *
from DentistRoll.models import Dentist
register = template.Library()



def dentist_total_cases(id):
    dentist_obj = Dentist.objects.get(id = id)
    case_obj = Case.objects.filter(dentist = dentist_obj)
    total = len(case_obj)
    print(total)
    return total

register.filter('dentist_total_cases', dentist_total_cases)