from django import template
from Case.models import Case
from ManagerRoll.models import Manager
from PlannerRoll.models import Planner
from TechnicianRoll.models import Technician
register = template.Library()

@register.simple_tag
def get_expense(type,user_id,case_id):
    if type == "manager":
        user_obj = Manager.objects.get(id=user_id)
        case_obj = Case.objects.get(id=case_id)
        if user_obj.fee:
            total_fee = (float(user_obj.fee)/100)*float(case_obj.totel_fee)
            round_off_value = round(total_fee, 2)
            return round_off_value
        else:
            return 0
    elif type == "planner":
        user_obj = Planner.objects.get(id=user_id)
        case_obj = Case.objects.get(id=case_id)
        total_plan = case_obj.treatment_plan_upper + case_obj.treatment_plan_lower
        planner_fee = user_obj.fee
        if user_obj.fee:
            total_fee = total_plan*planner_fee
            return total_fee
        else:
            return 0
    elif type == "technician":
        user_obj = Technician.objects.get(id=user_id)
        case_obj = Case.objects.get(id=case_id)

        total_aligners = case_obj.aligners_upper + case_obj.aligners_lower
        technician_fee = user_obj.fee
        if user_obj.fee:
            total_fee = technician_fee*total_aligners
            return total_fee
        else:
            return 0
register.filter('get_expense', get_expense)