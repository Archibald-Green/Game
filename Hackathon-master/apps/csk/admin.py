from django.contrib import admin

from .models import (
    UserCall, 
    MasterUser,
)


admin.site.register(UserCall)
admin.site.register(MasterUser)
