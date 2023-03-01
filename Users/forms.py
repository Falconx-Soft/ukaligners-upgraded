from django.contrib.auth.forms import UserCreationForm
from .models import Account
from django.forms import ModelForm

class CutomUserCreationForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ['username', 'email', 'password1', 'password2']


# class CutomUserEditForm(ModelForm):
#     class Meta:
#         model = Account
#         fields = ['username', 'email']

#         def __init__(self, *args, **kwargs):
#             super(CutomUserEditForm, self).__init__(*args, **kwargs)

#             for name, fields in self.fields.items():
#                 fields.widget.attrs.update({'class': 'form-control'})