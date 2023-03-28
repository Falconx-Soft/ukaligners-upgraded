from .models import Clinic
from django.forms import ModelForm

class ClinicForm(ModelForm):
    class Meta:
        model = Clinic
        exclude = ('user',)