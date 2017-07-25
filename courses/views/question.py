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

from gamification.models import ScoreManager

class QuestionVerificationView(SingleObjectMixin, FormView):
	template_name = 'courses/lesson/detail.html'
	form_class = AnswerForm
	model = Question

	def get_success_url(self):
		return reverse_lazy('courses:lesson_detail', kwargs={'course_slug': self.get_course().slug, 'slug': self.get_lesson().slug})
	
	def get_course(self):
		return Course.objects.filter(slug=self.kwargs['course_slug']).first()

	def get_lesson(self):
		return Lesson.objects.filter(slug=self.kwargs['lesson_slug']).first()

	def get_form(self, * args, ** kwargs):
		return self.form_class(self.object, *args, **kwargs)

	def post(self, request, * args, ** kwargs):
		self.object = self.get_object()
		form = self.get_form(request.POST, request.FILES)
		
		if form.is_valid() and self.form_valid(form):
			return HttpResponseRedirect(self.get_success_url() + "?next=true")
		else:
			return HttpResponseRedirect(self.get_success_url())
		

	def form_valid(self, form):
		answer = form.save(commit=False)
		answer.user = self.request.user
		answer.lesson = self.get_lesson()
		answer.question = self.get_object()
		answer.is_correct = set(list(  answer.question.choices.filter(is_correct=True)  )) == set(list(  form.cleaned_data['choices'] ))
		answer.save()
		form.save_m2m()
		
		score_manager = ScoreManager.objects.get_or_create(user=self.request.user)[0]

		if answer.is_correct:
			score_manager.up_xp(4)
			messages.success(self.request, _("You answer is correct!"))
		else:
			score_manager.up_xp(1)
			messages.error(self.request, _("You answer is incorrect! Try again..."))
		score_manager.save()
		return answer.is_correct