from .models import Case
from django.forms import ModelForm

class CaseForm(ModelForm):

    class Meta:
        model = Case
        exclude = ('refinement',)