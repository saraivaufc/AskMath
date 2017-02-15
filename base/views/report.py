from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from django.contrib import messages

from ..forms import ReportForm
from ..utils.constants import Constants

class ReportCreateView(CreateView):
	template_name = "dsd"
	form_class = ReportForm

	def get_success_url(self):
		return self.request.path

	def form_valid(self, form):
		form.instance.created_by = self.request.user
		form.instance.ip_address = self.request.META['REMOTE_ADDR']
		form.save()
		messages.success(self.request, Constants.REPORT_SUCCESS_SEND)
		return HttpResponseRedirect(form.instance.page)

	def form_invalid(self,form):
		messages.success(self.request, Constants.REPORT_ERROR_SEND)
		return HttpResponseRedirect(form.instance.page)		