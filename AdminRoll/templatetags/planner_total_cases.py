from django import template
from ..models import *
from Case.models import *
from SaloonRoll.models import *
register = template.Library()



def planner_total_cases(id):
    planner_obj = Planner.objects.get(id = id)
    case_obj = Case.objects.filter(planner = planner_obj)
    total = len(case_obj)
    print(total)
    return total

register.filter('planner_total_cases', planner_total_cases)