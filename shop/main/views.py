from django.http import HttpResponse
from django.shortcuts import redirect, render
from . import models, forms
from django.contrib import messages
from django.contrib.auth import authenticate, login
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from main import serializers, models

# Create your views here.
def index(request):
    
    return render(request, 'main/index.html')

def login(request):
    form = forms.UserLoginForm()
    if request.method == "POST":
        print("EMAIL: ", request.POST.get("email"))
        print("PASSWORD: ", request.POST.get("password"))
        
        form = forms.UserLoginForm(request.POST)
        
        if form.is_valid():
            user = models.User.objects.filter(email=request.POST.get("email"), password=request.POST.get("password")).exists()
            if user == True:
                return redirect('/index')
            else:
                form.add_error('email', 'Неправильный логин или пароль')
                
                for error in form.errors:
                    print(dir(error))

        return render(request, "main/log.html", context={'form': form})

    return render(request, 'main/log.html', context={'form': form})

def register(request):
    
    if request.method == "POST":
        
        login = request.POST.get("login")
        
        password = request.POST.get("password")
        
        email = request.POST.get("email")
        
        
        user = models.User(
            login = login,
            password = password,
            email = email,
        )
        
        form = forms.UserRegisterForm (request.POST)
        
        if form.is_valid(): 
            user.save()
            user = authenticate(request.POST)
            messages.success(request, f'Создан аккаунт {email}!')
            return redirect('/login')
        
        return HttpResponse("Invalid data") 
    return render(request, 'main/register.html')


class UserListView (generics.ListAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [IsAuthenticated]
    
    