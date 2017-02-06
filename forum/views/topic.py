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

from ..models import Category, Topic, Comment
from ..forms import TopicForm, CommentForm

class TopicListView(ListView):
	template_name = 'forum/topic/list.html'
	model = Topic
	paginate_by = settings.PAGINATE_BY

	def get_category(self):
		return Category.objects.filter(slug=self.kwargs['category_slug']).first()

	def get_queryset(self):
		"""Return the last topics issues."""
		return Topic.objects.filter(category=self.get_category(), status='p')

	def get_context_data(self, ** kwargs):
		context = super(TopicListView, self).get_context_data(** kwargs)
		context['category'] = self.get_category()
		return context

class TopicDetailView(SingleObjectMixin, ListView):
	template_name = 'forum/topic/detail.html'
	model = Topic
	paginate_by = settings.PAGINATE_BY

	def get_category(self):
		return Category.objects.filter(slug=self.kwargs['category_slug']).first()

	def get_queryset(self):
		return self.object.get_comments()

	def get_context_data(self, ** kwargs):
		context = super(TopicDetailView, self).get_context_data(** kwargs)
		context['category'] = self.get_category() 
		context['topic'] = self.object
		return context

	def get(self, request, * args, ** kwargs):
		self.object = self.get_object(queryset=self.get_category().get_topics())
		if not self.object.status == 'p':
			return HttpResponseForbidden()
		return super(TopicDetailView, self).get(request)

class TopicCreateView(CreateView):
	template_name = 'forum/topic/form.html'
	form_class = TopicForm

	def get_category(self):
		return Category.objects.filter(slug=self.kwargs['category_slug']).first()

	def get_success_url(self):
		return reverse_lazy('forum:topic_detail', kwargs={'category_slug': self.get_category().slug, 'slug': self.object.slug})


	def get_context_data(self, ** kwargs):
		context = super(TopicCreateView, self).get_context_data(** kwargs)
		context['category'] = self.get_category()
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
		form.instance.category = self.get_category()
		form.instance.status = 'p'
		topic = form.save()
		form_comment.instance.user = self.request.user
		form_comment.instance.topic = topic
		form_comment.instance.ip_address = self.request.META['REMOTE_ADDR']
		form_comment.save()
		return super(TopicCreateView, self).form_valid(form)

class TopicUpdateView(UpdateView):
	template_name = 'forum/topic/form.html'
	form_class = TopicForm
	model = Topic

	def get_category(self):
		return Category.objects.filter(slug=self.kwargs['category_slug']).first()

	def get_success_url(self):
		return reverse_lazy('forum:topic_detail', kwargs={'category_slug': self.get_category().slug, 'slug': self.object.slug})

	def get_context_data(self, ** kwargs):
		context = super(TopicUpdateView, self).get_context_data(** kwargs)
		context['category'] = self.get_category()
		context['comment_form'] = CommentForm(instance=self.object.get_comments().last())
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
		form_comment = CommentForm(request.POST, request.FILES, instance=self.object.get_comments().last())
		if form.is_valid() and form_comment.is_valid():
			return self.form_valid(form, form_comment)
		else:
			return self.form_invalid(form)

	def form_valid(self, form, form_comment):
		form.save()
		form_comment.instance.date = timezone.now()
		form_comment.instance.ip_address = self.request.META['REMOTE_ADDR']
		form_comment.save()
		return super(TopicUpdateView, self).form_valid(form)

class TopicDeleteView(DeleteView):
	template_name = 'forum/topic/check_delete.html'
	model = Topic

	def get_category(self):
		return Category.objects.filter(slug=self.kwargs['category_slug']).first()

	def get_success_url(self):
		return reverse_lazy('forum:topic_list', kwargs={'category_slug': self.get_category().slug})

	def get_context_data(self, ** kwargs):
		context = super(TopicDeleteView, self).get_context_data(** kwargs)
		context['category'] = self.get_category()
		return context

	def get(self, request, * args, ** kwargs):
		if not self.get_object().user == request.user:
			return HttpResponseForbidden()

		return super(TopicDeleteView, self).get(request)

	def post(self, request, * args, ** kwargs):
		if not self.get_object().user == request.user:
			return HttpResponseForbidden()

		topic = self.get_object()
		if not topic.user == request.user:
			return HttpResponseForbidden()
		topic.status = 'w'
		topic.save()
		return HttpResponseRedirect(self.get_success_url())