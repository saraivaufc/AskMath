# -*- coding: utf-8 -*-

from django.contrib import admin
from django.utils.translation import ugettext as _

from base.actions import (StatusAction, )

from .models import (Category, Topic, Comment)
from .forms import (CategoryForm)


class CategoryAdmin(admin.ModelAdmin, StatusAction):
	form = CategoryForm
	list_display = ('name', 'status', 'created_by', 'last_modified')
	search_fields = ['name']
	list_filter = ['status', 'last_modified']
	actions = []

	def save_model(self, request, obj, form, change):
		form.instance.created_by = request.user
		form.save()

class TopicAdmin(admin.ModelAdmin, StatusAction):
	list_display = ('title', 'status', 'created_by', 'last_modified')
	search_fields = ['title']
	list_filter = ['status', 'last_modified',]
	actions = []

	def save_model(self, request, obj, form, change):
		form.instance.created_by = request.user
		form.save()

class CommentAdmin(admin.ModelAdmin, StatusAction):
	model = Comment
	list_display = ('user', 'topic', 'text', 'status', 'created_by', 'last_modified')
	list_filter = ['user', 'topic', 'status', 'last_modified',]
	search_fields = ['text']
	actions = []

	def save_model(self, request, obj, form, change):
		form.instance.created_by = request.user
		form.save()

admin.site.register(Category, CategoryAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Comment, CommentAdmin)