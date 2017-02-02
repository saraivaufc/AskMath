from django.utils.translation import ugettext_lazy as _
from django.views.generic import FormView
from django.views.generic.detail import SingleObjectMixin
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect

from ask.models import Issue, Lesson, Question, Answer
from ask.forms import AnswerForm

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
		questions = list(self.get_lesson().questions.all().order_by('position'))
		questions_ = []
		for index, question in enumerate(questions):
			if not Answer.objects.filter(user=self.request.user, question=question, exists=True).exists():
				questions_.append(question)
		if not questions_:
			answer = Answer.objects.filter(user=self.request.user, lesson=self.get_lesson(), correct=False, exists=True).last()
			if answer:
				return answer.question

		print questions_
		if len(questions_) >= 1:
			return questions_[0]
		else:
			return None

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
		if not self.object:
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
		return super(QuestionDetailView, self).form_valid(form)