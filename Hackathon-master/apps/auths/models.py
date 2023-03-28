# Python
from typing import (
    Optional,
    Iterable
)
import random

# Django
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator



# Local
from abstracts.models import AbstractModel


class CustomUserManager(BaseUserManager):
    """ClientManager."""

    def create_user(
        self,
        username,
        phone_number,
        password: str,
        is_superuser = False
    ) -> 'CustomUser':
        if is_superuser == False:
            custom_user: 'CustomUser' = self.model(
                phone_number=phone_number,
                password=password
            )
        else:
            custom_user: 'CustomUser' = self.model(
                username=username,
                phone_number=phone_number,
                password=password
            )
        custom_user.set_password(password)
        custom_user.save(using=self._db)
        return custom_user
        


    # def create_superuser(
    #     self,
    #     username: str,
    #     password: str
    # ) -> 'CustomUser':
    #     print('==================== Ay')
    #     custom_user: 'CustomUser' = self.model(
    #         username=username,
    #         password=password
    #     )
    #     custom_user.phone_number = '+77712345677'
    #     custom_user.is_superuser = True
    #     custom_user.is_active = True
    #     custom_user.is_staff = True
    #     custom_user.set_password(password)
    #     custom_user.save(using=self._db)
    #     return
    

    def create_superuser(self, username, phone_number, password):
        custom_user = self.create_user(
            username,
            "+77712345677",
            password,
            is_superuser=True
        )
        print('==================== Ay')
        custom_user.is_superuser=True
        custom_user.is_active = True
        custom_user.is_staff = True
        custom_user.save(using=self._db)

        return custom_user


class CustomUser(
    AbstractBaseUser, 
    PermissionsMixin,
    AbstractModel
):
    """My custom user."""

    full_name = models.CharField(
        verbose_name='ФИО',
        max_length=255,
        null=True,
        blank=True
    )
    username = models.CharField(
        verbose_name='Никнейм',
        max_length=255,
        null=True,
        blank=True,
        unique=True
    )
    phone_regex = RegexValidator(
        regex=r'^\(?\+[0-9]{1,3}\)? ?-?[0-9]{1,3} ?-?[0-9]{3,5} ?-?[0-9]{4}( ?-?[0-9]{3})? ?(\w{1,10}\s?\d{1,6})?', 
        message="Phone number must be entered in the format: '+77777777777'. Up to 15 digits allowed."
    )
    phone_number = models.CharField(
        validators=[phone_regex], 
        max_length=17, 
        blank=True
    )
    is_superuser = models.BooleanField(
        verbose_name='superuser',
        default=False
    )
    is_active = models.BooleanField(
        verbose_name='active',
        default=True
    )
    is_staff = models.BooleanField(
        verbose_name='staff',
        default=False
    )
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['phone_number']

    objects = CustomUserManager()

    class Meta:
        ordering = ('-datetime_created',)
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def save(self, *args: tuple, **kwargs: dict) -> None:
        self.full_clean()
        return super().save(*args, **kwargs)
    def __str__(self):
        return str(self.phone_number)
    



