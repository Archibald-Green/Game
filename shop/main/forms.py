from django import forms
from main import models

class UserLoginForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ('email', 'password',)
        widgets = {
            
        }

class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ('login','password','email',)