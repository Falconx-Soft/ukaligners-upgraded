from .models import Technician
from django.forms import ModelForm

class TechnicianForm(ModelForm):
    class Meta:
        model = Technician
        exclude = ('user',)