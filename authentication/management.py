from authentication.models import User
from django.contrib.auth.models import Permission
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType

group_permissions = {
	"student": [
	
	],
	"teacher": [
		
	],
	"assistant": [
		
	],
	"administrator": [
	
	]
}

def create_user_groups(sender, **kwargs):
	print "Initialising data post_migrate"

	for group in group_permissions:
		model = User
		content_type = ContentType.objects.get_for_model(model)
		role, created = Group.objects.get_or_create(name=group)
		for perm in group_permissions[group]:
			try:
				perm = Permission.objects.get(codename=perm)
			except Exception, e:
				print e, ">>" ,perm
				continue
			role.permissions.add(perm)
		role.save()