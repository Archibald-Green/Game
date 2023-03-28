# from django import forms
# from main import models

# class UserLoginForm(forms.ModelForm):
#     class Meta:
#         model = models.User
#         fields = ('email', 'password',)
#         widgets = {
            
#         }

# class UserRegisterForm(forms.ModelForm):
#     class Meta:
#         model = models.User
#         fields = ('login','password','email',)

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from main.models import CustomUser , Book, BookPage

# Sign Up Form
class SignUpForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput (attrs={'class': 'form-input'}),)
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}),)
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}),)
    email = forms.CharField(label='email ', widget=forms.EmailInput(attrs={'class': 'form-input'}),)

    def clean(self):
        print("GDE TY???????", self.cleaned_data)
        if self.cleaned_data['password1'] == self.cleaned_data['password2']:
            self.cleaned_data['password'] = self.cleaned_data['password1']

        return super(UserCreationForm, self).clean()

    def save(self, commit=False):
        print("SYUDA ZASHEL!!!")

        CustomUser.objects.create_user(
            self.cleaned_data['email'], 
            self.cleaned_data['username'], 
            self.cleaned_data['password'], 
        )

        return super().save(commit)

    class Meta:
        model = CustomUser
        fields = ('username', 'email')
        widgets = {
            'username': forms.TextInput (attrs={'class': 'form-input'}),
            'password': forms.PasswordInput(attrs={'class': 'form-input'}),
            'email': forms.EmailInput(attrs={'class': 'form-input'}),
        }


class CustomLoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password')


class BookPageForm(forms.ModelForm):
    class Meta:
        model = BookPage
        fields = "__all__"
        
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
