from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta(UserCreationForm.Meta):
        fields = ['email', 'username', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    class Meta:
        fields = ['username', 'password']


class LogoutForm(forms.Form):
    pass
