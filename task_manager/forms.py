from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class SignupForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name')


class SighInForm(AuthenticationForm):

    class Meta:
        model = get_user_model()
        fields = ('username', 'password')

