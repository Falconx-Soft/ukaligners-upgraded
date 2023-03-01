from .models import Saloon_owner, Saloon
from django.forms import ModelForm
from django import forms

class Saloon_ownerForm(ModelForm):
    saloon = forms.ModelMultipleChoiceField(
            queryset=Saloon.objects.all(),
            widget=forms.CheckboxSelectMultiple,
            required=False)
    class Meta:
        model = Saloon_owner
        exclude = ('user','surname')

class SaloonForm(ModelForm):

    class Meta:
        model = Saloon
        fields = '__all__'