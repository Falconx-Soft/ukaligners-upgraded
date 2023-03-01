from .models import Planner
from django.forms import ModelForm

class PlannerForm(ModelForm):
    class Meta:
        model = Planner
        exclude = ('user',)