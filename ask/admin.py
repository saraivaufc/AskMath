# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.admin import AdminSite

from base.actions import (StatusAction, )

from .models import (Issue, Lesson, Question, Choice, Answer, Video)
from .forms import (IssueForm, LessonForm, QuestionForm, ChoiceForm, AnswerForm, VideoForm, )

class IssueAdmin(admin.ModelAdmin, StatusAction):
	form = IssueForm
	list_display = ('name', 'status', 'last_modified')
	list_filter = ['status', 'creation', 'last_modified']
	search_fields = ['name', 'status']
	actions = []

	def save_model(self, request, obj, form, change):
		form.instance.created_by = request.user
		form.save()

class LessonAdmin(admin.ModelAdmin, StatusAction):
	form = LessonForm
	list_display = ('name', 'status', 'last_modified')
	list_filter = ['issues', 'status', 'creation', 'last_modified']
	search_fields = ['name', 'status']
	filter_horizontal = ['issues', 'requirements','questions', 'videos', ]
	actions = []

	def save_model(self, request, obj, form, change):
		form.instance.created_by = request.user
		form.save()


class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 0

class QuestionAdmin(admin.ModelAdmin):
	form = QuestionForm
	extra = 1
	list_display = ('text', 'last_modified')
	inlines = [
		ChoiceInline,
	]

	def save_model(self, request, obj, form, change):
		form.instance.created_by = request.user
		form.save()

class AnswerAdmin(admin.ModelAdmin):
	list_display = ('user', 'lesson', 'question','correct','exists', 'last_modified')
	list_filter = ['user', 'lesson', 'question','correct','exists', 'last_modified']

class VideoAdmin(admin.ModelAdmin):
	form = VideoForm
	list_display = ('title', 'position', 'url', 'last_modified')
	search_fields = ['title', 'description', 'creation', 'last_modified']
	actions = []

	def save_model(self, request, obj, form, change):
		form.instance.created_by = request.user
		form.save()

admin.site.register(Issue, IssueAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Video, VideoAdmin)