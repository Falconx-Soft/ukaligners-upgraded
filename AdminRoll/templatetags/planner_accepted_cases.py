from django import template
from ..models import *
from Case.models import *
from SaloonRoll.models import *
register = template.Library()



def planner_accepted_cases(id):
    planner_obj = Planner.objects.get(id = id)
    case_obj_accept = Case.objects.filter(planner = planner_obj, status = 'accepted')
    case_obj_tc = Case.objects.filter(planner = planner_obj, status = 'tc')
    case_obj_treatment = Case.objects.filter(planner = planner_obj, status = 'treatment')
    total = len(case_obj_accept) + len(case_obj_tc) + len(case_obj_treatment)
    print(total)
    return total

register.filter('planner_accepted_cases', planner_accepted_cases)