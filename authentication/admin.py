from django.contrib import admin
from django.contrib.auth.models import Permission
from authentication.models import (User,)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
	pass

@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
	list_filter = ('content_type', )