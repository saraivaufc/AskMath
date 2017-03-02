# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseForbidden
from django.http import HttpResponseRedirect
from django.conf import settings
from django.utils import timezone
from django.contrib.messages.views import SuccessMessageMixin


from ..models import Category, Topic, Comment
from ..forms import CommentForm

class CommentCreateView(SuccessMessageMixin, CreateView):
	template_name = 'forum/comment/form.html'
	model = Comment
	form_class = CommentForm
	success_message = _(u"Comment created successfully")

	def get_success_url(self):
		return reverse_lazy('forum:topic_detail', kwargs={'slug': self.get_topic().slug})

	def get_topic(self):
		return Topic.objects.filter(slug=self.kwargs['topic_slug']).first()

	def get_context_data(self, ** kwargs):
		context = super(CommentCreateView, self).get_context_data(** kwargs)
		context['topic'] = self.get_topic()
		return context

	def form_valid(self, form):
		form.instance.user = self.request.user
		form.instance.created_by = self.request.user
		form.instance.topic = self.get_topic()
		form.instance.date = timezone.now()
		form.instance.status = 'p'
		form.instance.ip_address = self.request.META['REMOTE_ADDR']
		form.save()
		return super(CommentCreateView, self).form_valid(form)

class CommentUpdateView(SuccessMessageMixin, UpdateView):
	template_name = 'forum/comment/form.html'
	model = Comment
	form_class = CommentForm
	success_message = _(u"Comment updated successfully")
	
	def get_success_url(self):
		return reverse_lazy('forum:topic_detail', kwargs={'slug': self.get_topic().slug})

	def get_topic(self):
		return Topic.objects.filter(slug=self.kwargs['topic_slug']).first()

	def get_context_data(self, ** kwargs):
		context = super(CommentUpdateView, self).get_context_data(** kwargs)
		context['topic'] = self.get_topic()
		return context

	def get(self, request, * args, ** kwargs):
		if not self.get_object().user == request.user or self.get_object().pk == self.get_object().topic.get_comments().first().pk:
			return HttpResponseForbidden()
		return super(CommentUpdateView, self).get(request, * args, ** kwargs)

	def post(self, request, * args, ** kwargs):
		if not self.get_object().user == request.user or self.get_object().pk == self.get_object().topic.get_comments().first().pk:
			return HttpResponseForbidden()
		return super(CommentUpdateView, self).post(request, * args, ** kwargs)

	def form_valid(self, form):
		comment = self.get_object()
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
		form.instance.ancient = ancient

		form.instance.user = self.request.user
		form.instance.last_modified = timezone.now()
		form.instance.ip_address = self.request.META['REMOTE_ADDR']
		form.save()
		return super(CommentUpdateView, self).form_valid(form)

class CommentDeleteView(DeleteView):
	template_name = 'forum/comment/check_delete.html'
	model = Comment

	def get_success_url(self):
		return reverse_lazy('forum:topic_detail', kwargs={'slug': self.get_topic().slug})

	def get_topic(self):
		return Topic.objects.filter(slug=self.kwargs['topic_slug']).first()

	def get_context_data(self, ** kwargs):
		context = super(CommentDeleteView, self).get_context_data(** kwargs)
		context['topic'] = self.get_topic()
		return context

	def get(self, request, * args, ** kwargs):
		self.object = self.get_object()
		if not self.object.user == request.user and not self.object.pk == self.object.topic.get_comments().first().pk and not request.user.has_perm('forum.delete_comment'):
			return HttpResponseForbidden()
		return super(CommentDeleteView, self).get(request)

	def post(self, request, * args, ** kwargs):
		self.object = self.get_object()
		if not self.object.user == request.user and not self.object.pk == self.object.topic.get_comments().first().pk and not request.user.has_perm('forum.delete_comment'):
			return HttpResponseForbidden()
		comment = self.object
		comment.status = 'r'
		comment.save()
		return HttpResponseRedirect(self.get_success_url())