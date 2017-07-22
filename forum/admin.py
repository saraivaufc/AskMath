# -*- coding: utf-8 -*-

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import (Category, Topic, Comment)
from .forms import (CategoryForm)


class CategoryAdmin(admin.ModelAdmin):
	form = CategoryForm
	list_display = ('name', 'status', 'created_by', 'last_modified')
	search_fields = ['name']
	list_filter = ['status', 'last_modified']
	actions = []

	def save_model(self, request, obj, form, change):
		form.instance.created_by = request.user
		form.save()

class TopicAdmin(admin.ModelAdmin):
	list_display = ('title', 'status', 'last_modified')
	search_fields = ['title']
	list_filter = ['status', 'last_modified',]
	actions = []

	def save_model(self, request, obj, form, change):
		form.instance.created_by = request.user
		form.save()

class CommentAdmin(admin.ModelAdmin):
	model = Comment
	list_display = ('text', 'user', 'topic' , 'status', 'creation')
	list_filter = ['user', 'topic', 'status', 'creation',]
	search_fields = ['text']
	actions = []

	def save_model(self, request, obj, form, change):
		form.instance.created_by = request.user
		form.save()

admin.site.register(Category, CategoryAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Comment, CommentAdmin)