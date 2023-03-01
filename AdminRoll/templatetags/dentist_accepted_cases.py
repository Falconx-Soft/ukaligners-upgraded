from django import template
from ..models import *
from Case.models import *
from DentistRoll.models import Dentist
register = template.Library()



def dentist_accepted_cases(id):
    dentist_obj = Dentist.objects.get(id = id)
    case_accept = Case.objects.filter(dentist = dentist_obj, status = 'accepted')
    case_tc = Case.objects.filter(dentist = dentist_obj, status = 'tc')
    case_treatment = Case.objects.filter(dentist = dentist_obj, status = 'treatment')
    total = len(case_accept) + len(case_tc) + len(case_treatment)
    return total

register.filter('dentist_accepted_cases', dentist_accepted_cases)