from django.contrib import admin

from main import models
# from .models import Book
# from main.models import User

# Register your models here.
admin.site.register(models.CustomUser)
admin.site.register(models.Book)
admin.site.register(models.BookPage)
admin.site.register(models.PageLink)
