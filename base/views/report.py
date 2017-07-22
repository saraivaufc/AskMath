from django.utils.translation import ugettext_lazy as _
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy

from ..forms import ReportForm
from ..models import Report, SocialNetwork

class ReportCreateView(SuccessMessageMixin, CreateView):
	template_name = "base/report.html"
	model = Report
	fields = ['name', 'email', 'message',]
	success_url = reverse_lazy('base:home')
	success_message = _("Message send success")

	def get_context_data(self, ** kwargs):
		context = super(ReportCreateView, self).get_context_data(** kwargs)
		context['social_networks'] = SocialNetwork.objects.all()
		return context

	def form_valid(self, form):
		form.instance.created_by = self.request.user if self.request.user.is_authenticated() else None 
		form.instance.ip_address = self.request.META['REMOTE_ADDR']
		form.save()
		return super(ReportCreateView, self).form_valid(form)