from django.contrib import admin
from django.contrib.auth.models import User, Group, Permission
from authentication.models import (User,)

class UserAdmin(admin.ModelAdmin):
	pass

class GroupAdmin(admin.ModelAdmin):
	pass

class PermissionAdmin(admin.ModelAdmin):
	pass

admin.site.register(User, UserAdmin)
#admin.site.register(Group, GroupAdmin)
admin.site.register(Permission, PermissionAdmin)
