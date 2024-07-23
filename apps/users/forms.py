from django import forms
from . import models


class RegisterForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ('username', 'password', 'email', )

        labels = {
            'username': 'Имя пользователя',
            'password': 'Пароль пользователя',
            'email': 'Электронная почта'
        }


class LoginForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ('username', 'password')

        labels = {
            'username': 'Имя пользователя',
            'password': 'Пароль',
        }
        widgets = {
            'password': forms.PasswordInput(),
            'email': forms.EmailInput()
        }
