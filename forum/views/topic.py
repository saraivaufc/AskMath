# -*- coding: utf-8 -*-

from __future__ import unicode_literals


from django.utils.translation import ugettext_lazy as _
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView, SingleObjectMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormMixin
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseForbidden
from django.http import HttpResponseRedirect
from django.conf import settings
from django.utils import timezone
from django.contrib.messages.views import SuccessMessageMixin

from ..models import Category, Topic, Comment
from ..forms import TopicForm, CommentForm

class TopicListView(ListView):
	template_name = 'forum/topic/list.html'
	model = Topic
	paginate_by = settings.PAGINATE_BY

	def get_queryset(self):
		category = self.request.GET.get(_("category"))
		if category:
			return Topic.objects.filter(category__slug=category, status='p')
		else:
			return Topic.objects.filter(status='p')

	def get_context_data(self, ** kwargs):
		context = super(TopicListView, self).get_context_data(** kwargs)
		context['categories'] = Category.objects.filter(status='p')
		return context

class TopicDetailView(DetailView):
	template_name = 'forum/topic/detail.html'
	model = Topic

	def get_context_data(self, ** kwargs):
		context = super(TopicDetailView, self).get_context_data(** kwargs)
		context['categories'] = Category.objects.filter(status='p')
		return context

class TopicCreateView(SuccessMessageMixin, CreateView):
	template_name = 'forum/topic/form.html'
	form_class = TopicForm
	model = Topic
	success_message = _(u"Topic created successfully")
	
	def get_success_url(self):
		return reverse_lazy('forum:topic_detail', kwargs={'slug': self.object.slug})

	def get_context_data(self, ** kwargs):
		context = super(TopicCreateView, self).get_context_data(** kwargs)
		context['comment_form'] = CommentForm()
		return context

	def post(self, request, * args, ** kwargs):
		form = self.get_form()
		form_comment = CommentForm(request.POST, request.FILES)
		if form.is_valid() and form_comment.is_valid():
			return self.form_valid(form, form_comment)
		else:
			return self.form_invalid(form)

	def form_valid(self, form, form_comment):
		form.instance.user = self.request.user
		form.instance.created_by = self.request.user
		form.instance.status = 'p'
		topic = form.save()
		form_comment.instance.user = self.request.user
		form_comment.instance.created_by = self.request.user
		form_comment.instance.topic = topic
		form_comment.instance.ip_address = self.request.META['REMOTE_ADDR']
		form_comment.instance.status = 'p'
		form_comment.save()
		return super(TopicCreateView, self).form_valid(form)

class TopicUpdateView(SuccessMessageMixin, UpdateView):
	template_name = 'forum/topic/form.html'
	form_class = TopicForm
	model = Topic
	success_message = _(u"Topic updated successfully")

	def get_success_url(self):
		return reverse_lazy('forum:topic_detail', kwargs={'slug': self.object.slug})

	def get_context_data(self, ** kwargs):
		context = super(TopicUpdateView, self).get_context_data(** kwargs)
		context['comment_form'] = CommentForm(instance=self.object.get_comments().first())
		return context

	def get(self, request, * args, ** kwargs):
		if not self.get_object().user == request.user:
			return HttpResponseForbidden()
		return super(TopicUpdateView, self).get(request)

	def post(self, request, * args, ** kwargs):
		if not self.get_object().user == request.user:
			return HttpResponseForbidden()
			
		self.object = self.get_object()
		form = self.get_form()
		form_comment = CommentForm(request.POST, request.FILES, instance=self.object.get_comments().first())
		if form.is_valid() and form_comment.is_valid():
			return self.form_valid(form, form_comment)
		else:
			return self.form_invalid(form)

	def form_valid(self, form, form_comment):
		comment = Comment.objects.get(pk=form_comment.instance.pk)
		
		ancient = Comment(
			user = comment.user,
			topic = comment.topic,
			text = comment.text,
			status = 'r',
			created_by = comment.created_by,
			creation = comment.creation,
			last_modified = comment.last_modified,
			ip_address =comment.ip_address,
		)
		ancient.save()
		form_comment.instance.ancient = ancient
		form_comment.instance.user = self.request.user
		form_comment.instance.last_modified = timezone.now()
		form_comment.instance.ip_address = self.request.META['REMOTE_ADDR']
		form_comment.save()
		form.save()
		return super(TopicUpdateView, self).form_valid(form)

class TopicDeleteView(DeleteView):
	template_name = 'forum/topic/check_delete.html'
	model = Topic
	success_message = _(u"Topic removed successfully")
	success_url = reverse_lazy('forum:topic_list')

	def get_context_data(self, ** kwargs):
		context = super(TopicDeleteView, self).get_context_data(** kwargs)
		return context

	def get(self, request, * args, ** kwargs):
		if not self.get_object().user == request.user and not request.user.has_perm('forum.delete_topic'):
			return HttpResponseForbidden()
		return super(TopicDeleteView, self).get(request)

	def post(self, request, * args, ** kwargs):
		if not self.get_object().user == request.user and not request.user.has_perm('forum.delete_topic'):
			return HttpResponseForbidden()
		self.object = self.get_object()
		topic = self.get_object()
		topic.status = 'r'
		topic.save()
		return HttpResponseRedirect(self.get_success_url())