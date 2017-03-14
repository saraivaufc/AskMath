# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.admin import AdminSite

from base.actions import (StatusAction, )

from .models import (Course, Lesson, Question, Choice, Answer, Video, Introduction, )
from .forms import (CourseForm, LessonForm, QuestionForm, AnswerForm, VideoForm, IntroductionForm,)

class CourseAdmin(admin.ModelAdmin, StatusAction):
	form = CourseForm
	list_display = ('name', 'status', 'created_by', 'last_modified')
	list_filter = ['status', 'creation', 'last_modified']
	search_fields = ['name']
	actions = []

	def save_model(self, request, obj, form, change):
		form.instance.created_by = request.user
		form.save()

class LessonAdmin(admin.ModelAdmin, StatusAction):
	form = LessonForm
	list_display = ('name', 'status', 'created_by', 'last_modified')
	list_filter = ['courses', 'status', 'last_modified']
	search_fields = ['name']
	filter_horizontal = ['courses', 'requirements','questions', 'videos', ]
	actions = []

	def save_model(self, request, obj, form, change):
		form.instance.created_by = request.user
		form.save()

class ChoiceInline(admin.TabularInline):
	model = Choice
	fields = ['text','is_correct',]
	extra = 0

class QuestionAdmin(admin.ModelAdmin):
	form = QuestionForm
	extra = 1
	list_display = ('text', 'created_by', 'last_modified')
	list_filter = ['last_modified',]
	search_fields = ['text']

	inlines = [
		ChoiceInline,
	]

	def save_model(self, request, obj, form, change):
		form.instance.created_by = request.user
		form.save()

class AnswerAdmin(admin.ModelAdmin):
	list_display = ('user', 'lesson', 'question','correct','exists', 'created_by', 'last_modified')
	list_filter = ['user', 'lesson', 'question','correct','exists', 'last_modified']

	def save_model(self, request, obj, form, change):
		form.instance.created_by = request.user
		form.save()

class VideoAdmin(admin.ModelAdmin):
	form = VideoForm
	list_display = ('title', 'position', 'url', 'created_by', 'last_modified')
	list_filter = ['last_modified']
	search_fields = ['title', 'description']
	actions = []

	def save_model(self, request, obj, form, change):
		form.instance.created_by = request.user
		form.save()

class IntroductionAdmin(admin.ModelAdmin):
	form = IntroductionForm
	list_display = ('text',)
	list_filter = ['last_modified']
	search_fields = ['text']

	def save_model(self, request, obj, form, change):
		form.instance.created_by = request.user
		form.save()

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Introduction, IntroductionAdmin)