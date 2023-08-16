from .models import TaskUser
from django.contrib.auth.forms import UserCreationForm
from task_manager.meta import get_meta
from django import forms


class SignupForm(UserCreationForm):

    password1 = forms.CharField(
        label=get_meta().get('Users').get('Password'),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=get_meta().get('Main').get('Pass1HelpText'),
    )

    class Meta(UserCreationForm.Meta):
        model = TaskUser
        fields = ['first_name', 'last_name', 'username',
                  'password1', 'password2']
