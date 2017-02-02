from django.utils.translation import ugettext_lazy as _
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect

import collections

from ask.models import Issue, Lesson, Question, Answer
from ask.utils.functions import lists_to_list

class LessonSorting():
	def __init__(self, lessons):
		self.__lessons = lessons
		self.__level_lesson = {}
		self.__index_level = 1

	def visit(self, lesson):
		if lesson in lists_to_list(self.__level_lesson.values()):
			return

		requirements = lesson.requirements.filter(status='p')
		if (set( lists_to_list(self.__level_lesson.values()) )).issuperset(set(requirements)):	
			if requirements:
				max_level = max(map(lambda x: self.get_level_lesson(x) , requirements)) 
				self.__index_level += max_level + 1

			if not self.__level_lesson.has_key(self.__index_level):
				self.__level_lesson[self.__index_level] = []
			self.__level_lesson[self.__index_level].append(lesson)
		else:
			for requirement in requirements:
				self.visit(requirement)

	def get_level_lesson(self, lesson):
		for level, lessons in self.__level_lesson.items():
			if lesson in lessons:
				return level
		return 0

	def get(self):
		while len(self.__lessons) > len(lists_to_list(self.__level_lesson.values())):
			for lesson in self.__lessons:
				self.visit(lesson)
		return self.__level_lesson

class LessonListView(ListView):
	template_name = 'ask/lesson/list.html'
	model = Lesson

	def get_issue(self):
		return Issue.objects.filter(slug=self.kwargs['issue_slug']).first()

	def get_queryset(self):
		"""Return the last published lessons."""
		lessons = list(Lesson.objects.filter(issues=self.get_issue(), status='p'))
		lessons = LessonSorting(lessons).get()
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
		if not self.get_object().status == 'p':
			raise PermissionDenied
		return super(LessonFinishedView, self).get(request)

	def post(self, request, * args, ** kwargs):
		lesson = self.get_object()
		Answer.objects.filter(user=request.user, lesson=lesson).update(exists=False)
		return HttpResponseRedirect(reverse_lazy('ask:answer_question', kwargs={'issue_slug': self.get_issue().slug, 'lesson_slug': lesson.slug}))