# -*- coding: utf-8 -*-

from __future__ import unicode_literals


from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseForbidden, HttpResponseRedirect

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView, SingleObjectMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormMixin

from django.conf import settings
from django.utils import timezone

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin


from ..models import Category, Topic, Comment
from ..forms import TopicForm, CommentForm

from gamification.models import ScoreManager


class TopicListView(ListView):
	template_name = 'forum/topic/list.html'
	model = Topic
	paginate_by = settings.PAGINATE_BY

	def get_context_data(self, ** kwargs):
		context = super(TopicListView, self).get_context_data(** kwargs)
		context['categories'] = Category.objects.filter(status=Category.PUBLISHED)
		
		category_slug = self.request.GET.get(_("category"))
		if category_slug:
			context['category_selected'] = Category.objects.filter(slug=category_slug, status=Category.PUBLISHED).first()	
		return context

	def get_queryset(self):
		category_slug = self.request.GET.get(_("category"))
		if category_slug:
			return Topic.objects.filter(category__slug=category_slug, status=Topic.PUBLISHED)
		else:
			return Topic.objects.filter(status=Topic.PUBLISHED)

class TopicDetailView(SingleObjectMixin, ListView):
	template_name = 'forum/topic/detail.html'
	model = Topic
	paginate_by = settings.PAGINATE_BY

	def get(self, request, * args, ** kwargs):
		self.object = self.get_object(queryset=Topic.objects.all())
		return super(TopicDetailView, self).get(request, * args, ** kwargs)

	def get_queryset(self):
		return Comment.objects.filter(topic=self.object, status=Comment.PUBLISHED)

class TopicCreateView(SuccessMessageMixin, CreateView):
	template_name = 'forum/topic/form.html'
	form_class = TopicForm
	model = Topic
	success_message = _("Topic created successfully")
	
	def get_success_url(self):
		return reverse_lazy('forum:topic_detail', kwargs={'slug': self.object.slug})

	def form_valid(self, form):
		form.instance.user = self.request.user
		form.instance.status = Topic.PUBLISHED
		form.instance.ip_address = self.request.META['REMOTE_ADDR']
		topic = form.save()
		score_manager = ScoreManager.objects.get_or_create(user=self.request.user)[0]
		score_manager.up_xp(10)
		score_manager.save()

		return super(TopicCreateView, self).form_valid(form)

class TopicUpdateView(SuccessMessageMixin, UpdateView):
	template_name = 'forum/topic/form.html'
	form_class = TopicForm
	model = Topic
	success_message = _("Topic updated successfully")

	def get_success_url(self):
		return reverse_lazy('forum:topic_detail', kwargs={'slug': self.object.slug})

	def get(self, request, * args, ** kwargs):
		if not self.get_object().user == request.user:
			return HttpResponseForbidden()
		return super(TopicUpdateView, self).get(request)

	def post(self, request, * args, ** kwargs):
		if not self.get_object().user == request.user:
			return HttpResponseForbidden()
		return super(TopicUpdateView, self).post(request)

class TopicDeleteView(SuccessMessageMixin, DeleteView):
	template_name = 'forum/topic/check_delete.html'
	model = Topic
	success_message = _("Topic removed successfully")
	success_url = reverse_lazy('forum:topic_list')

	def get_context_data(self, ** kwargs):
		context = super(TopicDeleteView, self).get_context_data(** kwargs)
		return context

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
		topic = self.get_object()
		topic.status = Topic.PUBLISHED
		topic.save()

		score_manager = ScoreManager.objects.get_or_create(user=self.request.user)[0]
		score_manager.down_xp(10)
		score_manager.save()
		
		messages.success(request, self.success_message)		
		return HttpResponseRedirect(self.get_success_url())