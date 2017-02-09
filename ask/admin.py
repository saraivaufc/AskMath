# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.admin import AdminSite

from base.actions import (StatusAction, )

from .models import (Issue, Lesson, Question, Choice, Answer, Video)
from .forms import (IssueForm, LessonForm, QuestionForm, ChoiceForm, AnswerForm, VideoForm, )

class IssueAdmin(admin.ModelAdmin, StatusAction):
	form = IssueForm
	list_display = ('name', 'status' )
	list_filter = ['status']
	search_fields = ['name', 'status']
	actions = []

	def save_model(self, request, obj, form, change):
		form.instance.created_by = request.user
		form.save()

class LessonAdmin(admin.ModelAdmin, StatusAction):
	form = LessonForm
	list_display = ('name', 'status')
	list_filter = ['issues', 'status', ]
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
	list_display = ('position', 'text', 'date')
	inlines = [
		ChoiceInline,
	]

	def save_model(self, request, obj, form, change):
		form.instance.created_by = request.user
		form.save()

class AnswerAdmin(admin.ModelAdmin):
	list_display = ('user', 'lesson', 'question','correct','exists', 'date')
	list_filter = ['user', 'lesson', 'question','correct','exists', 'date']

class VideoAdmin(admin.ModelAdmin, StatusAction):
	form = VideoForm
	list_display = ('position', 'title', 'url', 'status', )
	list_filter = ['status']
	search_fields = ['title', 'description']
	actions = []

	def save_model(self, request, obj, form, change):
		form.instance.created_by = request.user
		form.save()

admin.site.register(Issue, IssueAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Video, VideoAdmin)