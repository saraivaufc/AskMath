from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm, UserChangeForm, UserCreationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from authentication.models import User
from django.conf import settings
from django.contrib import messages

from ..utils.constants import Constants
from ..forms import UserForm

class UserCreateView(CreateView):
	template_name = 'authentication/account/register.html'
	form_class = UserForm
	success_url = reverse_lazy('authentication:account_login')

	def form_valid(self, form):
		user = form.save(commit=False)
		user.set_password(user.password)
		user.save(group="student")
		messages.success(self.request, Constants.USER_SUCCESS_CREATED)
		return super(UserCreateView, self).form_valid(form)


class UserDetailView(DetailView):
	template_name = 'authentication/account/detail.html'
	model = User
	
	def get_context_data(self, ** kwargs):
		context = super(UserDetailView, self).get_context_data( ** kwargs)
		return context

class UserUpdateView(UpdateView):
	template_name = 'authentication/account/form.html'
	model = User
	fields = ['first_name', 'last_name', 'profile_image', 'email']

	def get_success_url(self):
		return reverse_lazy('authentication:account_detail', kwargs={'pk': self.object.pk})

	def get(self, request, * args, ** kwargs):
		user = self.get_object()
		if not request.user == user:
			return HttpResponseForbidden()
		return super(UserUpdateView, self).get(request)

	def post(self, request, * args, ** kwargs):
		user = self.get_object()
		if not request.user == user:
			return HttpResponseForbidden()
		return super(UserUpdateView, self).post(request)
	
	def form_valid(self, form):
		return super(UserUpdateView, self).form_valid(form)

class UserDeleteView(DeleteView):
	template_name = 'authentication/account/check_delete.html'
	model = User
	success_url = reverse_lazy('authentication:account_login')

	def get(self, request, * args, ** kwargs):
		user = self.get_object()
		if not request.user == user:
			return HttpResponseForbidden()
		return super(UserDeleteView, self).get(request)

	def post(self, request, * args, ** kwargs):
		user = self.get_object()
		if not request.user == user:
			return HttpResponseForbidden()
		return super(UserDeleteView, self).post(request)