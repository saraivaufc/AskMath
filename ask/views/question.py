from django.utils.translation import ugettext_lazy as _
from django.views.generic import FormView
from django.views.generic.detail import SingleObjectMixin
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages

from ask.models import Issue, Lesson, Question, Answer
from ask.forms import AnswerForm
from ask.utils.constants import Constants
from ask.utils.lesson import get_question_of_lesson

class QuestionDetailView(SingleObjectMixin, FormView):
	template_name = 'ask/question/detail.html'
	form_class = AnswerForm
	model = Answer
	
	def get_issue(self):
		return Issue.objects.filter(slug=self.kwargs['issue_slug']).first()

	def get_lesson(self):
		return Lesson.objects.filter(slug=self.kwargs['lesson_slug']).first()

	def get_success_url(self):
		return reverse_lazy('ask:answer_question', kwargs={'issue_slug': self.get_issue().slug, 'lesson_slug': self.get_lesson().slug})

	def get_object(self):
		return get_question_of_lesson(self.request.user, self.get_lesson())

	def get_form(self, * args, ** kwargs):
		return self.form_class(self.object, *args, **kwargs)

	def get_context_data(self, ** kwargs):
		context = super(QuestionDetailView, self).get_context_data(** kwargs)
		context['issue'] = self.get_issue()
		context['lesson'] = self.get_lesson()
		return context

	def get(self, request, * args, ** kwargs):
		if not self.get_issue().status == 'p' or not self.get_lesson().status == 'p':
			raise PermissionDenied
		self.object = self.get_object()
		if not self.object and self.get_lesson().questions.all():
			return HttpResponseRedirect(reverse_lazy('ask:lesson_finished', kwargs={'issue_slug': self.get_issue().slug, 'slug': self.get_lesson().slug } ))
		return super(QuestionDetailView, self).get(request)

	def post(self, request, * args, ** kwargs):
		if not self.get_issue().status == 'p' or not self.get_lesson().status == 'p':
			raise PermissionDenied
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
		answer.lesson = self.get_lesson()
		answer.question = self.get_object()
		answer.correct = set(list(  answer.question.get_choices().filter(is_correct=True)  )) == set(list(  form.cleaned_data['choices'] ))
		answer.save()
		form.save_m2m()
		if answer.correct:
			messages.success(self.request, Constants.ANSWER_CORRECT)
		else:
			messages.error(self.request, Constants.ANSWER_INCORRECT)
		return super(QuestionDetailView, self).form_valid(form)