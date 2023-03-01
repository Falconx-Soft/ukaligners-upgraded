from .models import Dentist, Clinic
from django.forms import ModelForm
from django import forms

class DentistForm(ModelForm):
    clinic = forms.ModelMultipleChoiceField(
            queryset=Clinic.objects.all(),
            widget=forms.CheckboxSelectMultiple,
            required=False)
    class Meta:
        model = Dentist
        exclude = ('user','surname')

class ClinicForm(ModelForm):

    class Meta:
        model = Clinic
        fields = '__all__'