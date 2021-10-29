from django.forms import *
from firstapp.models import *


class LoginForm(MogelForm):
    class Meta:
        model = User
        fields = ['name',"surname",'patronymic','login','password']
        widgets = {
            "name":TextInput(attrs = {
                'placeholder': "Введите ваше имя"
            }),
            "surname": TextInput(attrs = {
                'placeholder': "Введите вашу фамилию"
            }),
            "patronymic": TextInput(attrs = {
                'placeholder': "Введите ваше имя"
            }),
            "login": TextInput(attrs = {
                'placeholder': "Введите ваше имя"
            }),
            "Password": PasswordInput(attrs = {
                'placeholder': "Введите ваш пароль"
            })
        }
