from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponseForbidden

from django.views.generic.list import ListView
from django.views.generic.detail import SingleObjectMixin, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from django.conf import settings

from ..models import Challenge, Solution
from ..forms import SolutionForm

class ChallengeListView(ListView):
	template_name = 'competition/challenge/list.html'
	model = Challenge
	paginate_by = settings.PAGINATE_BY

	def get_queryset(self):
		return Challenge.objects.filter(status=Challenge.PUBLISHED)

class ChallengeDetailView(SingleObjectMixin, ListView):
	template_name = 'competition/challenge/detail.html'
	model = Challenge
	paginate_by = settings.PAGINATE_BY

	def get(self, request, * args, ** kwargs):
		self.object = self.get_object(queryset=Challenge.objects.all())
		return super(ChallengeDetailView, self).get(request, * args, ** kwargs)

	def get_context_data(self, ** kwargs):
		context = super(ChallengeDetailView, self).get_context_data( ** kwargs)
		context['challenge'] = self.object
		return context

	def get_queryset(self):
		return Solution.objects.filter(challenge=self.object)

class SolutionCreateView(SuccessMessageMixin, CreateView):
	template_name = 'competition/challenge/solution/form.html'
	model = Solution
	form_class = SolutionForm
	success_message = _("Solution created successfully")

	def get_success_url(self):
		return reverse_lazy('competition:challenge_detail', kwargs={"slug": self.get_challenge().slug})

	def get_challenge(self):
		return Challenge.objects.filter(slug=self.kwargs['challenge_slug']).first()

	def get_context_data(self, ** kwargs):
		context = super(SolutionCreateView, self).get_context_data( ** kwargs)
		context["challenge"] = self.get_challenge()
		return context

	def form_valid(self, form):
		form.instance.challenge = self.get_challenge()
		form.instance.user = self.request.user
		return super(SolutionCreateView, self).form_valid(form)

class SolutionUpdateView(SuccessMessageMixin, UpdateView):
	template_name = 'competition/challenge/solution/form.html'
	model = Solution
	form_class = SolutionForm
	success_message = _("Solution changed successfully")

	def get_challenge(self):
		return Challenge.objects.filter(slug=self.kwargs['challenge_slug']).first()

	def get_success_url(self):
		return reverse_lazy("competition:challenge_detail", kwargs={'slug': self.get_challenge().slug})

	def get_context_data(self, ** kwargs):
		context = super(SolutionUpdateView, self).get_context_data(** kwargs)
		context['challenge'] = self.get_challenge()
		return context

	def get(self, request, * args, ** kwargs):
		self.object = self.get_object()
		if not self.object.user == request.user or self.object.is_correct:
			return HttpResponseForbidden()
		return super(SolutionUpdateView, self).get(request)

	def post(self, request, * args, ** kwargs):
		self.object = self.get_object()
		if not self.object.user == request.user or self.object.is_correct:
			return HttpResponseForbidden()
		return super(SolutionUpdateView, self).post(request)

class SolutionDeleteView(DeleteView):
	template_name = 'competition/challenge/solution/check_delete.html'
	model = Solution
	success_message = _("Solution removed successfully")

	def get_challenge(self):
		return Challenge.objects.filter(slug=self.kwargs['challenge_slug']).first()
	
	def get_success_url(self):
		return reverse_lazy("competition:challenge_detail", kwargs={'slug': self.get_challenge().slug})

	def get_context_data(self, ** kwargs):
		context = super(SolutionDeleteView, self).get_context_data(** kwargs)
		context['challenge'] = self.get_challenge()
		return context
	
	def get(self, request, * args, ** kwargs):
		self.object = self.get_object()
		if not self.object.user == request.user:
			return HttpResponseForbidden()
		return super(SolutionDeleteView, self).get(request)

	def post(self, request, * args, ** kwargs):
		self.object = self.get_object()
		if not self.object.user == request.user:
			return HttpResponseForbidden()
		messages.success(request, self.success_message)
		return super(SolutionDeleteView, self).post(request)