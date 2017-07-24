# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import (Course, Lesson, LearningObject, LearningObjectHistory, Question, Choice, Answer, Video, )
from .forms import (CourseForm, LessonForm, QuestionForm, AnswerForm, VideoForm,)

class CourseAdmin(admin.ModelAdmin):
	form = CourseForm
	list_display = ['position', 'name', 'status', 'last_modified']
	list_display_links = ['name']
	list_editable = ['position']

	list_filter = ['status', 'creation', 'last_modified']
	search_fields = ['name']

	def save_model(self, request, obj, form, change):
		form.instance.created_by = request.user
		form.save()

class LearningObjectInline(admin.TabularInline):
	model = LearningObject
	fields = ['position', 'question', 'video']
	raw_id_fields = ['question', 'video']
	extra = 0

class LessonAdmin(admin.ModelAdmin):
	form = LessonForm
	list_display = ('name', 'status', 'created_by', 'last_modified')
	list_filter = ['courses', 'status', 'last_modified']
	search_fields = ['name']
	filter_horizontal = ['courses', 'requirements',]

	class Media:
		js = ("base/packages/jquery-2.1.3.min.js", "courses/packages/jquery-sortable.js", "courses/js/sortable.js",)
	
	inlines = [
		LearningObjectInline, 
	]

	def save_model(self, request, obj, form, change):
		form.instance.created_by = request.user
		form.save()

class LearningObjectHistoryAdmin(admin.ModelAdmin):
	model = LearningObjectHistory
	list_display = ('user', 'learning_object', 'active', 'creation')
	list_filter = ['learning_object__lesson', 'active', 'creation']
	search_fields = []

class ChoiceInline(admin.TabularInline):
	model = Choice
	fields = ['position', 'text','is_correct',]
	extra = 0

class QuestionAdmin(admin.ModelAdmin):
	form = QuestionForm
	extra = 0
	list_display = ('text', 'created_by', 'creation')
	list_filter = ['creation',]
	search_fields = ['text']

	class Media:
		js = ("base/packages/jquery-2.1.3.min.js", "courses/packages/jquery-sortable.js", "courses/js/sortable.js",)

	inlines = [
		ChoiceInline,
	]

	def save_model(self, request, obj, form, change):
		form.instance.created_by = request.user
		form.save()

class AnswerAdmin(admin.ModelAdmin):
	list_display = ('user', 'lesson', 'question','is_correct','exists', 'creation')
	list_filter = ['user', 'lesson', 'question','is_correct','exists', 'creation']

	def save_model(self, request, obj, form, change):
		form.instance.created_by = request.user
		form.save()

class VideoAdmin(admin.ModelAdmin):
	form = VideoForm
	list_display = ('title', 'url', 'created_by', 'creation')
	list_filter = ['creation']
	search_fields = ['title', 'description']

	def save_model(self, request, obj, form, change):
		form.instance.created_by = request.user
		form.save()

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(LearningObjectHistory, LearningObjectHistoryAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Video, VideoAdmin)