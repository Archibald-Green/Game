from django.db import models
from django.forms import ImageField
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, User
)

# Create your models here.
# class User(models.Model):
#     login = models.CharField("Логин пользователя", max_length=255, blank = True)
    
#     password = models.CharField("Пароль пользователя", max_length=255, blank = True)
    
#     email = models.EmailField("Почта", max_length=255, blank = True)


# class Plots(models.Model):
    
#     title = models.CharField ('Место', blank = True)
    
#     plot= models.TextField('Сюжеты',blank =True)
    
# class Locatins(models.Model):
    
#     location = models.ImageField(upload_to='/')



class MyUserManager(BaseUserManager):
    def create_user(self, email, username, password):
        print('Работай')
        if not email:
            raise ValueError("ENTER AN EMAIL BUDDY")
        if not username:
            raise ValueError("I KNOW YOU HAVE A NAME")
        if not password:
            raise ValueError("PASSWORD?!?!?!? HELLO??")

        Role.objects.get_or_create(name="пользователь")
        role = Role.objects.get(name="пользователь")
        user = self.model(
             email = self.normalize_email(email),
             username = username,
             role = role
             )
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self, username, password, alias=None):
        Role.objects.get_or_create(name="администратор")
        role = Role.objects.get(name="администратор")
        user = self.model(
            username=username,
            role=role
        )
        user.is_admin = True
        user.set_password(password)
        user.save()
        return user
    
    def is_saler(self):
        return self.model.role
    
        



class Role(models.Model):
    name = models.CharField("Наименование роли", max_length=50)

    class Meta:
        verbose_name = "Роль"
        verbose_name_plural = "Роли"
    
    def __str__(self):
        return self.name


class CustomUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='Адрес email',
        max_length=255,
        unique=True,
    )

    role = models.ForeignKey(Role, verbose_name="Роль пользователя", on_delete=models.CASCADE)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()
    
    username = models.CharField(
        verbose_name='login',
        max_length=255,
        unique=True,
    )

    USERNAME_FIELD = 'username'
    
    def is_saler(self):
        return self.model.role

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class Book (models.Model):
    
    title = models.TextField(name ='title', unique= True)
    first_page = models.ForeignKey('BookPage', null = True,blank=True, on_delete=models.SET_NULL, related_name = 'first_page')
    def __str__(self):
        return '{self.title} ({self.id})'.format(self=self)
    
class BookPage(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE,)
    title = models.TextField(name ='title')
    body =models.TextField(name='body')
    cover_art = models.ImageField(upload_to='book_images', null =True, blank=True)
    def __str__(self):
        return '{self.title} ({self.id})'.format(self=self)
    
class PageLink(models.Model):
    from_page = models.ForeignKey(BookPage, on_delete=models.CASCADE)
    to_page = models.ForeignKey(BookPage, related_name ='to_page', on_delete=models.CASCADE,)
    name = models.TextField()
    def __str__(self):
        return '{self.from_page.title} -> {self.to_page.title} ({self.id})'.format(self=self)
    
    
    class Meta:
        unique_together = ['from_page', 'to_page']
        
class BoolProgress (models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    book_page = models.ForeignKey(BookPage, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ['user', 'book']
        
    @classmethod
    def start_reading(cls, user, book):
        progress = BoolProgress(user = user, book = book, book_page = book.first_page)
        progress.save()
        return progress