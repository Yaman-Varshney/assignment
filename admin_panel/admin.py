from django.contrib import admin
from admin_panel.models import Resident, Employee, Event
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class UserInline(admin.StackedInline) :
    model = Employee
    can_delete = False
    verbose_name_plural = 'Users'

class CustomisedUserAdmin(UserAdmin) :
    inlines = (UserInline,)

admin.site.unregister(User)
admin.site.register(User, CustomisedUserAdmin)
admin.site.register(Resident)
admin.site.register(Event)