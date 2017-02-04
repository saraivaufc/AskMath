from django.utils.translation import ugettext_lazy as _
from django.views.generic.list import ListView
from django.views.generic.edit import FormMixin
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages

from ..models import SocialNetwork
from ..forms import ContactForm
from ..utils.constants import Constants

class ContactListView(FormMixin, ListView):
	template_name = 'base/contact.html'
	model = SocialNetwork
	form_class = ContactForm
	success_url = reverse_lazy("base:contact")

	def post(self, request, * args, ** kwargs):
		form = self.get_form()
		if form.is_valid():
			return self.form_valid(form)
		else:
			return self.form_invalid(form)

	def form_valid(self, form):
		contact = form.cleaned_data
		#Enviar mensagem para email aqui
		messages.success(self.request, Constants.MESSAGE_SUCCESS_SEND)
		return super(ContactListView, self).form_valid(form)

	def form_invalid(self,form):
		messages.error(self.request, Constants.MESSAGE_ERROR_SEND)
		return super(ContactListView, self).form_valid(form)