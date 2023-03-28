# Python
from typing import (
    Optional,
    Any,
    Mapping,
    Union,
    Dict,
    Type
)

# Django
from django.forms import (
    ModelForm,
    Form,
    PasswordInput,
    CharField,
    EmailField
)

# Local
from auths.models import CustomUser


class RegistrationForm(ModelForm):
    """Registration form for CustomUser."""
    
    password2 = CharField(
        label='Повторите пароль',
        max_length=100,
        widget=PasswordInput()
    )

    class Meta:
        model = CustomUser
        fields = (
            'full_name',
            'phone_number',
            'password'
        )
        widgets = {
            'password': PasswordInput(
                attrs={'class': 'psd'}
            ),
        }

    def save(self, commit: bool = ...) -> CustomUser:
        self.full_clean()
        return super().save(commit)


class LoginForm(Form):
    """Login form for CustomUser."""
    
    phone_number = CharField(
        label='Номер телефона',
        max_length=100
    )
    password = CharField(
        label='Пароль',
        max_length=100,
        widget=PasswordInput()
    )
    class Meta:
        model = CustomUser
        fields = (
            'phone_number',
            'password'
        )
