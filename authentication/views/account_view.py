from django.utils.translation import ugettext_lazy as _

from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.contrib import messages
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse


from django.utils.http import urlsafe_base64_encode
from django.core.mail import EmailMultiAlternatives
from django.utils.encoding import force_text, force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string

import datetime

from authentication.models import User
from authentication import settings as local_settings

from ..forms import UserCreationForm, UserChangeForm

class AccountCreateView(SuccessMessageMixin, CreateView):
	template_name = 'authentication/account/register.html'
	form_class = UserCreationForm
	success_url = reverse_lazy('authentication:account_login')
	success_message = _("Account created successfully.")

	def form_valid(self, form):
		user = form.save(commit=False)
		user.set_password(user.password)
		if local_settings.CONFIRM_EMAIL:
			user.is_active = False
			self.send_account_activation_email(self.request, user)
			messages.success(self.request, _("Please, check your email to activate account."))
		else:
			user.is_active = True
		if local_settings.DEFAULT_GROUP:
			user.save(group=local_settings.DEFAULT_GROUP)
		else:
			user.save()
		return super(AccountCreateView, self).form_valid(form)

	def send_account_activation_email(self, request, user):
		text_content = _('Account Activation Email')
		subject = _('Email Activation')
		template_name = "authentication/account/activation.html"
		from_email = settings.DEFAULT_FROM_EMAIL
		recipients = [user.email]
		kwargs = {
			"uidb64": urlsafe_base64_encode(force_bytes(user.pk)).decode(),
			"token": default_token_generator.make_token(user)
		}
		activation_url = reverse("authentication:account_activate", kwargs=kwargs)
		activate_url = "{0}://{1}{2}".format(request.scheme, request.get_host(), activation_url)

		context = {
			'user': user,
			'activate_url': activate_url
		}

		html_content = render_to_string(template_name, context)
		email = EmailMultiAlternatives(subject, text_content, from_email, recipients)
		email.attach_alternative(html_content, "text/html")
		email.send()


class AccountDetailView(DetailView):
	template_name = 'authentication/account/detail.html'
	model = User

	def get(self, request, * args, ** kwargs):
		user = self.get_object()
		if not request.user == user:
			return HttpResponseForbidden()
		return super(AccountDetailView, self).get(request)
	
	def get_context_data(self, ** kwargs):
		context = super(AccountDetailView, self).get_context_data( ** kwargs)
		return context

class AccountUpdateView(UpdateView):
	template_name = 'authentication/account/form.html'
	model = User
	form_class = UserChangeForm

	def get_success_url(self):
		return reverse_lazy('authentication:account_detail', kwargs={'pk': self.object.pk})

	def get(self, request, * args, ** kwargs):
		user = self.get_object()
		if not request.user == user:
			return HttpResponseForbidden()
		return super(AccountUpdateView, self).get(request)

	def post(self, request, * args, ** kwargs):
		user = self.get_object()
		if not request.user == user:
			return HttpResponseForbidden()
		return super(AccountUpdateView, self).post(request)
	
	def form_valid(self, form):
		return super(AccountUpdateView, self).form_valid(form)

class AccountDeleteView(DeleteView):
	template_name = 'authentication/account/check_delete.html'
	model = User
	success_url = reverse_lazy('authentication:account_login')

	def get(self, request, * args, ** kwargs):
		user = self.get_object()
		if not request.user == user:
			return HttpResponseForbidden()
		return super(AccountDeleteView, self).get(request)

	def post(self, request, * args, ** kwargs):
		user = self.get_object()
		if user and not request.user == user:
			return HttpResponseForbidden()
		user.is_active = False
		user.save()
		logout(request)
		return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)

class AccountActivateView(View):
	def get(self, request, * args, ** kwargs):
		uidb64 = request.GET.get('uidb64')
		token = request.GET.get('token')
		try:
			uid = force_text(urlsafe_base64_decode(uidb64))
			user = User.objects.get(pk=uid)
		except User.DoesNotExist:
			user = None
		if user and default_token_generator.check_token(user, token):
			user.is_active = True
			user.save()
			login(request, user)
			return HttpResponseRedirect(reverse_lazy("authentication:account_login"))
		else:
			return HttpResponse(_("Activation link has expired"))