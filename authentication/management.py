from authentication.models import User
from django.contrib.auth.models import Permission
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType

group_permissions = {
	"administrator": [
		#Base
			#SocialNetwork
			'add_socialnetwork', 'change_socialnetwork', 'delete_socialnetwork', 
		#Authentication
			#User
			'change_user',
		#FlatPages
			#FlatPage
			'add_flatpage', 'change_flatpage', 'delete_flatpage', 
		#Sites
			#Site
			'add_site', 'change_site', 'delete_site',
		#Ask
			#Issue
			'add_issue', 'change_issue', 'delete_issue', 
			#Lesson
			'add_lesson', 'change_lesson', 'delete_lesson',
			#Question
			'add_question', 'change_question', 'delete_question',
			#Choice
			'add_choice', 'change_choice', 'delete_choice',
			#Introduction
			'add_introduction', 'change_introduction', 'delete_introduction',
			#Video
			'add_video', 'change_video', 'delete_video',
			#Answer
			'change_answer',
		#Forum
			#category
			'add_category', 'change_category', 'delete_category',
			#topic
			'delete_topic',
			#comment
			'delete_comment',
	],
	"teacher": [
		#Ask
			#Issue
			'add_issue', 'change_issue', 'delete_issue', 
			#Lesson
			'add_lesson', 'change_lesson', 'delete_lesson',
			#Question
			'add_question', 'change_question', 'delete_question',
			#Choice
			'add_choice', 'change_choice', 'delete_choice',
			#Introduction
			'add_introduction', 'change_introduction', 'delete_introduction',
			#Video
			'add_video', 'change_video', 'delete_video',
			#Answer
			'change_answer',
		#Forum
			#category
			'add_category', 'change_category', 'delete_category',
			#topic
			'delete_topic',
			#comment
			'delete_comment',
	],
	"assistant": [
		#Ask
			#Issue
			'add_issue', 'change_issue', 'delete_issue', 
			#Lesson
			'add_lesson', 'change_lesson', 'delete_lesson',
			#Question
			'add_question', 'change_question', 'delete_question',
			#Choice
			'add_choice', 'change_choice', 'delete_choice',
			#Introduction
			'add_introduction', 'change_introduction', 'delete_introduction',
			#Video
			'add_video', 'change_video', 'delete_video',
		#Forum
			#category
			'add_category', 'change_category', 'delete_category',
			#topic
			'delete_topic',
			#comment
			'delete_comment',
	],
	"student": [
	
	]
}

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
				perm = Permission.objects.get(codename=perm)
			except Exception, e:
				print e, ">>" ,perm
				continue
			role.permissions.add(perm)
		role.save()