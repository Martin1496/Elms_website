# from django.contrib.auth.models import User
# from django import forms
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
#
# class RegistrationForm(UserCreationForm):
#     email = forms.EmailField(required=True)
#
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password1', 'password2')
#
# class LoginForm(AuthenticationForm):
#     username = forms.CharField(label='Username', max_length=50)
#     password = forms.CharField(widget=forms.PasswordInput)
#
# class LogoutForm(forms.Form):
#     pass
