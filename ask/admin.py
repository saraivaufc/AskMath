# -*- coding: utf-8 -*-

from django.contrib import admin
from django.utils.translation import ugettext as _
from django.contrib.admin import AdminSite

from base.actions import (StatusAction, )

from .models import (Issue, Lesson, Question, Choice, Answer)
from .forms import (IssueForm, LessonForm, QuestionForm, ChoiceForm, AnswerForm)

class IssueAdmin(admin.ModelAdmin, StatusAction):
	form = IssueForm
	list_display = ('name', 'status' )
	list_filter = ['status']
	search_fields = ['name', 'status']
	actions = []

class LessonAdmin(admin.ModelAdmin, StatusAction):
	form = LessonForm
	list_display = ('name', 'status', )
	list_filter = ['issues', 'status', ]
	search_fields = ['name', 'status']
	filter_horizontal = ['issues', 'requirements','questions']
	actions = []


class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 0

class QuestionAdmin(admin.ModelAdmin):
	form = QuestionForm
	extra = 1

	inlines = [
		ChoiceInline,
	]

class AnswerAdmin(admin.ModelAdmin):
	list_display = ('user', 'lesson', 'question','correct','exists', 'date')
	list_filter = ['user', 'lesson', 'question','correct','exists', 'date']

admin.site.register(Issue, IssueAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)