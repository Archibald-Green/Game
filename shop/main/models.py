from django.db import models

# Create your models here.
class User(models.Model):
    login = models.CharField("Логин пользователя", max_length=255, blank = True)
    
    password = models.CharField("Пароль пользователя", max_length=255, blank = True)
    
    email = models.EmailField("Почта", max_length=255, blank = True)
    

# class Plots(models.Model):
    
#     title = models.CharField ('Место', blank = True)
    
#     plot= models.TextField('Сюжеты',blank =True)
    
# class Locatins(models.Model):
    
#     location = models.ImageField(upload_to='/')

# class Book (models.Model):
#     '''Interactive function'''
#     title = models.TextField(name ='title', blank = False, unique= True)
    
