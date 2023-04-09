from django.contrib import admin

from main import models
# from .models import Book
# from main.models import User

class Admin(admin.ModelAdmin):
    filter_horizontal = ('Items',)
    
    
admin.site.register(models.CustomUser)
admin.site.register(models.Book)
admin.site.register(models.BookPage)
admin.site.register(models.PageLink)
admin.site.register(models.Item)
admin.site.register(models.BoolProgress)