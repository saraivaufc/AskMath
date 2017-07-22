from django.contrib.auth.models import Permission
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType

from authentication import settings as local_settings
from .models import User

permissions = local_settings.PERMISSIONS
group_permissions = local_settings.GROUP_PERMISSIONS

def create_user_groups(sender, **kwargs):
	print "Initialising data post_migrate"
	groups_visited = []
	for group in group_permissions:
		model = User
		content_type = ContentType.objects.get_for_model(model)
		role, created = Group.objects.get_or_create(name=group)
		if not role in groups_visited:
			groups_visited.append(role)
			role.permissions.clear()
			
		for perm in group_permissions[group]:
			try:
				perm, created = Permission.objects.get_or_create(codename=perm, name=permissions[perm], content_type=content_type)
			except Exception, e:
				print e, ">>" ,perm
				continue
			role.permissions.add(perm)
		role.save()