from .models import TaskUser
from ..meta import get_meta
from django.contrib.auth.forms import UserCreationForm
from django import forms


class SignupForm(UserCreationForm):

    password1 = forms.CharField(
        label=get_meta().get('Users').get('Password'),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=get_meta().get('Users').get('Pass1HelpText'),
    )

    password2 = forms.CharField(
        label=get_meta().get('Users').get('PasswordApproval'),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=get_meta().get('Users').get('PasswordConfReq'),
    )

    class Meta(UserCreationForm.Meta):
        model = TaskUser
        fields = ['first_name', 'last_name', 'username',
                  'password1', 'password2']

        labels = {
            'first_name': get_meta().get('Users').get('FirstName'),
            'last_name': get_meta().get('Users').get('LastName'),
            'username': get_meta().get('Users').get('UserName'),
        }

        help_texts = {
            'username': get_meta().get('Users').get('UserNameReq'),
            'password2': get_meta().get('Users').get('PasswordConfReq')
        }
