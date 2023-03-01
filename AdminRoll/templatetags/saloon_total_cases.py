from django import template
from ..models import *
from Case.models import *
from SaloonRoll.models import *
register = template.Library()



def saloon_total_cases(id):
    saloon_owner_obj = Saloon_owner.objects.get(id = id)
    case_obj = Case.objects.filter(saloon_owner = saloon_owner_obj)
    total = len(case_obj)
    print(total)
    return total

register.filter('saloon_total_cases', saloon_total_cases)