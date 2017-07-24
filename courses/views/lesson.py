# -*- coding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _
from django.http import HttpResponseForbidden
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
import collections

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from courses.models import Course, Lesson, LearningObject, LearningObjectHistory, Question, Answer
from courses.forms.question import AnswerForm
from courses.utils.lesson import LessonSorting, get_question_of_lesson

from gamification.models import ScoreManager

class LessonListView(ListView):
	template_name = 'courses/lesson/list.html'
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

class LessonDetailView(DetailView):
	template_name = 'courses/lesson/detail.html'
	model = Lesson

	def get_course(self):
		return Course.objects.filter(slug=self.kwargs['course_slug']).first()

	def get_context_data(self, ** kwargs):
		learning_object = self.get_learning_object_history().learning_object
		context = super(LessonDetailView, self).get_context_data(** kwargs)
		context['course'] = self.get_course()
		context['learning_object'] = learning_object
		context['percentage'] = self.get_percentage(self.request.user)
		#process
		if learning_object.question:
			context['form'] = AnswerForm(learning_object.question)
		return context

	def get(self, request, * args, ** kwargs):
		self.object = self.get_object()

		if self.get_percentage(request.user) == 100:
			return HttpResponseRedirect(reverse_lazy('courses:lesson_finished', kwargs={'course_slug': self.get_course().slug, 'slug': self.object.slug}))
					
		if self.request.GET.has_key("next") or self.request.GET.has_key("previous"):
			if self.request.GET.has_key("next") and not self.next_learning_object():
				learning_object_history = self.get_learning_object_history()
				learning_object_history.active = False
				learning_object_history.save()
			if self.request.GET.has_key("previous") and not self.previous_learning_object():
				print "Nao e possivel voltar"
			return HttpResponseRedirect(reverse_lazy('courses:lesson_detail', kwargs={'course_slug': self.get_course().slug, 'slug': self.object.slug}))
		else:
			return super(LessonDetailView, self).get(request)

	def get_percentage(self, user):
		if LearningObjectHistory.objects.filter(user=user, learning_object__lesson=self.object, active=False).exists() and not LearningObjectHistory.objects.filter(user=user, learning_object__lesson=self.object, active=True).exists():
			return 100
		else:
			learning_objects = list(LearningObject.objects.filter(lesson=self.object))
			current_learning_object = self.get_learning_object_history().learning_object
			index = learning_objects.index(current_learning_object)
			return (100 * index ) / len(learning_objects)

	def get_learning_object_history(self):
		learning_object_history = LearningObjectHistory.objects.filter(user=self.request.user, learning_object__lesson=self.object, active=True).first()
		if not learning_object_history:
			learning_object = LearningObject.objects.filter(lesson=self.object).order_by('position').first()
			if learning_object:
				learning_object_history = LearningObjectHistory.objects.create(user=self.request.user, learning_object=learning_object, active=True)
		return learning_object_history

	def next_learning_object(self):
		learning_object = self.get_learning_object_history().learning_object
		if learning_object.next:
			LearningObjectHistory.objects.create(user=self.request.user, learning_object=learning_object.next,active=True)
			return True
		else:
			return False

	def previous_learning_object(self):
		learning_object = self.get_learning_object_history().learning_object
		if learning_object.previous:
			LearningObjectHistory.objects.create(user=self.request.user, learning_object=learning_object.previous,active=True)
			return True
		else:
			return False


class LessonFinishedView(DetailView):
	template_name = 'courses/lesson/finished.html'
	model = Lesson

	def get_course(self):
		return Course.objects.filter(slug=self.kwargs['course_slug']).first()

	def get_context_data(self, ** kwargs):
		context = super(LessonFinishedView, self).get_context_data(** kwargs)
		context['course'] = self.get_course()
		return context

	def get(self, request, * args, ** kwargs):
		self.object = self.get_object()
		if not self.object.status == 'p':
			return HttpResponseForbidden()
		return super(LessonFinishedView, self).get(request)

	def post(self, request, * args, ** kwargs):
		self.object = self.get_object()
		learning_object = LearningObject.objects.filter(lesson=self.object).order_by('position').first()
		if learning_object:
			learning_object_history = LearningObjectHistory.objects.create(user=self.request.user, learning_object=learning_object, active=True)
		return HttpResponseRedirect(reverse_lazy('courses:lesson_detail', kwargs={'course_slug': self.get_course().slug, 'slug': self.object.slug}))