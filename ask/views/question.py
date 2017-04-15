from django.utils.translation import ugettext_lazy as _
from django.views.generic import FormView
from django.views.generic.list import ListView
from django.views.generic.detail import SingleObjectMixin
from django.http import HttpResponseForbidden
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages

from ..models import Course, Lesson, Question, Answer
from ..forms import AnswerForm, LessonForm
from ..utils.constants import Constants
from ..utils.lesson import get_question_of_lesson

from gamification.models import ScoreManager

class QuestionDetailView(SingleObjectMixin, FormView):
	template_name = 'ask/question/detail.html'
	form_class = AnswerForm
	model = Answer
	
	def get_course(self):
		return Course.objects.filter(slug=self.kwargs['course_slug']).first()

	def get_lesson(self):
		return Lesson.objects.filter(slug=self.kwargs['lesson_slug']).first()

	def get_success_url(self):
		return reverse_lazy('ask:answer_question', kwargs={'course_slug': self.get_course().slug, 'lesson_slug': self.get_lesson().slug})

	def get_object(self):
		return get_question_of_lesson(self.request.user, self.get_lesson())

	def get_form(self, * args, ** kwargs):
		return self.form_class(self.object, *args, **kwargs)

	def get_context_data(self, ** kwargs):
		context = super(QuestionDetailView, self).get_context_data(** kwargs)
		context['course'] = self.get_course()
		context['lesson'] = self.get_lesson()
		#total de questoes da licao
		context['questions_amount'] = len(self.get_lesson().questions.all())
		#total de questoes ja respondidas corretamente pelo usuario atual
		context['questions_corrects'] = len( filter(lambda question: question.get_answers().filter(user=self.request.user, correct=True, exists=True).exists(), self.get_lesson().questions.all()))
		#a porcentagem que conclusao da licao
		try:
			context['percent_completed'] = (context['questions_corrects'] * 100) / context['questions_amount']
		except ZeroDivisionError:
			context['percent_completed'] = 0
		return context

	def get(self, request, * args, ** kwargs):
		if not self.get_course().status == 'p' or not self.get_lesson().status == 'p':
			return HttpResponseForbidden()
		self.object = self.get_object()
		if not self.object and self.get_lesson().questions.all():
			return HttpResponseRedirect(reverse_lazy('ask:lesson_finished', kwargs={'course_slug': self.get_course().slug, 'slug': self.get_lesson().slug } ))
		return super(QuestionDetailView, self).get(request)

	def post(self, request, * args, ** kwargs):
		if not self.get_course().status == 'p' or not self.get_lesson().status == 'p':
			return HttpResponseForbidden()
		self.object = self.get_object()
		form = self.get_form(request.POST, request.FILES)
		if form.is_valid():
			return self.form_valid(form)
		else:
			return self.form_invalid(form)
		return super(QuestionDetailView, self).post(request)

	def form_valid(self, form):
		answer = form.save(commit=False)
		answer.user = self.request.user
		answer.created_by = self.request.user
		answer.lesson = self.get_lesson()
		answer.question = self.get_object()
		answer.correct = set(list(  answer.question.get_choices().filter(is_correct=True)  )) == set(list(  form.cleaned_data['choices'] ))
		answer.save()
		form.save_m2m()
		
		score_manager = ScoreManager.objects.get_or_create(user=self.request.user)[0]

		if answer.correct:
			score_manager.up_xp(4)
			messages.success(self.request, Constants.ANSWER_CORRECT)
		else:
			score_manager.up_xp(1)
			messages.error(self.request, Constants.ANSWER_INCORRECT)
		score_manager.save()
		return super(QuestionDetailView, self).form_valid(form)