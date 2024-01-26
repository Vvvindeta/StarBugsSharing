from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from users.models import User


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "username",
            "phone_number",
            "password1",
            "password2",
        )

    username = forms.CharField(
        label="Имя пользователя",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Введите ваше имя пользователя",
            }
        )
    )

    phone_number = forms.CharField(
        label="Номер телефона",
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "Введите ваш номер телефона",
            }
        )
    )

    password1 = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Введите ваш пароль",
            }
        )
    )
    password2 = forms.CharField(
        label="подтвердите пароль",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Подтвердите ваш пароль",
            }
        )
    )
