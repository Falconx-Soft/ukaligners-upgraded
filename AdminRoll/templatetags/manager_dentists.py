from django import template
from ..models import *
from Case.models import *
from SaloonRoll.models import *
register = template.Library()



def manager_dentists(id):
    manager_obj = Manager.objects.get(id = id)
    dentist_obj = Dentist.objects.filter(manager = manager_obj)
    Saloon_owner_obj = Saloon_owner.objects.filter(manager = manager_obj)
    total = len(dentist_obj) + len(Saloon_owner_obj)
    print(total)
    return total

register.filter('manager_dentists', manager_dentists)