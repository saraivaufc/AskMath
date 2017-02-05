# -*- coding: utf-8 -*-

from django.contrib import admin
from django.utils.translation import ugettext as _

from base.actions import (StatusAction, )

from .models import (Category, Topic, Comment)
from .forms import (CategoryForm)


class CategoryAdmin(admin.ModelAdmin, StatusAction):
	form = CategoryForm
	list_display = ('name', 'status')
	search_fields = ['name', 'status']
	actions = []

class TopicAdmin(admin.ModelAdmin, StatusAction):
	list_display = ('title', 'status')
	search_fields = ['title', 'status']
	actions = []

class CommentAdmin(admin.ModelAdmin):
	model = Comment
	list_display = ('user', 'topic', 'text')
	filter_fields = ['user', 'topic', 'date']
	actions = []

admin.site.register(Category, CategoryAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Comment, CommentAdmin)