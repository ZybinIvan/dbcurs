from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    # username = forms.CharField(verbose_name="Ник", max_length=20, null=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
