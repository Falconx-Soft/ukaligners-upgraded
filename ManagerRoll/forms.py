from .models import Manager
from django.forms import ModelForm

class ManagerForm(ModelForm):
    class Meta:
        model = Manager
        exclude = ('user',)