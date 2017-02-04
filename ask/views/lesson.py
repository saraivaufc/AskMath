# -*- coding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect

import collections

from ask.models import Issue, Lesson, Question, Answer
from ask.utils.lesson import LessonSorting, get_question_of_lesson

class LessonListView(ListView):
	template_name = 'ask/lesson/list.html'
	model = Lesson

	def get_issue(self):
		return Issue.objects.filter(slug=self.kwargs['issue_slug']).first()

	def get_queryset(self):
		"""Return the last published lessons."""
		lessons = Lesson.objects.filter(issues=self.get_issue(), status='p')
		lessons = LessonSorting(lessons).get_lessons()
		#print lessons
		levels = collections.OrderedDict(sorted(lessons.items()))
		return levels


	def get_context_data(self, ** kwargs):
		context = super(LessonListView, self).get_context_data(** kwargs)
		context['issue'] = self.get_issue()
		return context

class LessonDetailView(DetailView):
	template_name = 'ask/lesson/detail.html'
	model = Lesson

	def get_issue(self):
		return Issue.objects.filter(slug=self.kwargs['issue_slug']).first()

	def get_context_data(self, ** kwargs):
		context = super(LessonDetailView, self).get_context_data(** kwargs)
		context['issue'] = self.get_issue()
		return context

	def get(self, request, * args, ** kwargs):
		if not self.get_object().status == 'p':
			raise PermissionDenied
		return super(LessonDetailView, self).get(request)

class LessonFinishedView(DetailView):
	template_name = 'ask/lesson/finished.html'
	model = Lesson

	def get_issue(self):
		return Issue.objects.filter(slug=self.kwargs['issue_slug']).first()

	def get_context_data(self, ** kwargs):
		context = super(LessonFinishedView, self).get_context_data(** kwargs)
		context['issue'] = self.get_issue()
		return context

	def get(self, request, * args, ** kwargs):
		lesson = self.get_object()
		if not lesson.status == 'p':
			raise PermissionDenied
		if get_question_of_lesson(request.user, lesson):
			return HttpResponseRedirect(reverse_lazy('ask:answer_question', kwargs={'issue_slug': self.get_issue().slug, 'lesson_slug': lesson.slug}))
		return super(LessonFinishedView, self).get(request)

	def post(self, request, * args, ** kwargs):
		lesson = self.get_object()
		Answer.objects.filter(user=request.user, lesson=lesson).update(exists=False)
		return HttpResponseRedirect(reverse_lazy('ask:answer_question', kwargs={'issue_slug': self.get_issue().slug, 'lesson_slug': lesson.slug}))