from django.contrib import admin
from django.contrib.auth.models import User, Group, Permission
from authentication.models import (User,)

class UserAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'email', 'profile_image', 'date_joined')
	list_filter = ['date_joined', 'is_moderator', 'is_staff']
	search_fields = ['first_name', 'last_name', 'email',]

class GroupAdmin(admin.ModelAdmin):
	pass

class PermissionAdmin(admin.ModelAdmin):
	pass

admin.site.register(User, UserAdmin)
#admin.site.register(Group, GroupAdmin)
admin.site.register(Permission, PermissionAdmin)


