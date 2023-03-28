from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from .models import CustomUser
import logging


LOGGER = logging.getLogger(__name__)

class CustomBackend(ModelBackend):
    """
    Аутентификация пользователя может происходить через username или номер телефона
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        print("____________________________________________AUTH_BACK")
        phone_number = None
       
        if username is None:
            phone_number = kwargs.get('phone_number')
        if username is None or password is None:
            return
        if not isinstance(username, str):
            return
        
        # check that username doesnt have spaces
        username = username.lstrip().rstrip().replace(' ', '')

        
        if phone_number:
            user = CustomUser.objects.get(phone_number=phone_number)
        else:
            print("ELSE___________________________________") 
            user = CustomUser.objects.get(username=username)
            print("ELSE_______________ELSE_______________", user)
        if user is not None:
            LOGGER.info(f"Найден пользователь по номеру телефона - {username}")
            allow = check_password(password, user.password)
            print("PASSWORD_____________", allow)
            # или любой другой текст
            return

        return