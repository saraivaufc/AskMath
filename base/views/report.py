from django.utils.translation import ugettext_lazy as _
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from django.contrib import messages

from ..forms import ReportForm
from ..models import SocialNetwork
from ..utils.constants import Constants

class ReportCreateView(CreateView):
	template_name = "base/report.html"
	form_class = ReportForm

	def get_success_url(self):
		return self.request.path

	def get_context_data(self, ** kwargs):
		context = super(ReportCreateView, self).get_context_data(** kwargs)
		context['social_networks'] = SocialNetwork.objects.all()
		return context

	def form_valid(self, form):
		form.instance.created_by = self.request.user if self.request.user.is_authenticated() else None 
		form.instance.page = self.request.GET.get(_("page")) if self.request.GET.has_key(_("page")) else  self.request.path
		form.instance.ip_address = self.request.META['REMOTE_ADDR']
		form.save()
		messages.success(self.request, Constants.REPORT_SUCCESS_SEND)
		return HttpResponseRedirect(form.instance.page)

	def form_invalid(self,form):
		messages.success(self.request, Constants.REPORT_ERROR_SEND)
		return HttpResponseRedirect(form.instance.page)