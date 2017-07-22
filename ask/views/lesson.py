# -*- coding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponseForbidden
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
import collections

from ask.models import Course, Lesson, Question, Answer
from ask.utils.lesson import LessonSorting, get_question_of_lesson

class LessonListView(ListView):
	template_name = 'ask/lesson/list.html'
	model = Lesson

	def get_course(self):
		return Course.objects.filter(slug=self.kwargs['course_slug']).first()

	def get_queryset(self):
		"""Return the last published lessons."""
		lessons = Lesson.objects.filter(courses=self.get_course(), status='p')
		lessons = LessonSorting(lessons).get_lessons()
		levels = collections.OrderedDict(sorted(lessons.items()))
		return levels


	def get_context_data(self, ** kwargs):
		context = super(LessonListView, self).get_context_data(** kwargs)
		context['course'] = self.get_course()
		return context

class LessonFinishedView(DetailView):
	template_name = 'ask/lesson/finished.html'
	model = Lesson

	def get_course(self):
		return Course.objects.filter(slug=self.kwargs['course_slug']).first()

	def get_context_data(self, ** kwargs):
		context = super(LessonFinishedView, self).get_context_data(** kwargs)
		context['course'] = self.get_course()
		return context

	def get(self, request, * args, ** kwargs):
		lesson = self.get_object()
		if not lesson.status == 'p':
			return HttpResponseForbidden()
		if get_question_of_lesson(request.user, lesson):
			return HttpResponseRedirect(reverse_lazy('ask:answer_question', kwargs={'course_slug': self.get_course().slug, 'lesson_slug': lesson.slug}))
		return super(LessonFinishedView, self).get(request)

	def post(self, request, * args, ** kwargs):
		lesson = self.get_object()
		Answer.objects.filter(user=request.user, lesson=lesson).update(exists=False)
		return HttpResponseRedirect(reverse_lazy('ask:answer_question', kwargs={'course_slug': self.get_course().slug, 'lesson_slug': lesson.slug}))