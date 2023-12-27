from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

    def clean_email(self):
        email = self.cleaned_data['email'].lower()  # Получение и нормализация email
        if User.objects.filter(email=email).exists():  # Проверка на существование пользователя с таким email
            raise ValidationError("Email already exists")  # Вызов ошибки, если пользователь найден
        return email


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
