from django import template
from ..models import *
from Case.models import *
from SaloonRoll.models import *
register = template.Library()



def technician_cases(id):
    tech_obj = Technician.objects.get(id = id)
    case_obj = Case.objects.filter(technician = tech_obj)
    total = len(case_obj)
    print(total)
    return total

register.filter('technician_cases', technician_cases)