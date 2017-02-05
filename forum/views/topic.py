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

class TopicDetailView(SingleObjectMixin, FormMixin, ListView, ):
	template_name = 'forum/topic/detail.html'
	paginate_by = settings.PAGINATE_BY
	model = Topic
	form_class = CommentForm

	def get_category(self):
		return Category.objects.filter(slug=self.kwargs['category_slug']).first()

	def get_success_url(self):
		return reverse_lazy('forum:topic_detail', kwargs={'category_slug': self.get_category().slug, 'slug': self.object.slug})

	def get_queryset(self):
		return self.object.get_comments()

	def get_form(self, * args, ** kwargs):
		if self.kwargs.has_key("comment_id"):
			comment = Comment.objects.get(user=self.request.user, id=self.kwargs["comment_id"])
			if comment:
				return self.form_class(instance=comment, * args, ** kwargs)
		return super(TopicDetailView, self).get_form()

	def get_context_data(self, ** kwargs):
		context = super(TopicDetailView, self).get_context_data(** kwargs)
		context['category'] = self.get_category()
		context['topic'] = self.object
		context['form'] = self.get_form()
		if self.kwargs.has_key("comment_id"):
			context['comment_edit'] = True
		return context

	def get(self, request, * args, ** kwargs):
		self.object = self.get_object(queryset=self.get_category().get_topics())
		if not self.object.status == 'p':
			return HttpResponseForbidden()
		return super(TopicDetailView, self).get(request)

	def post(self, request, * args, ** kwargs):
		self.object = self.get_object(queryset=self.get_category().get_topics())
		form = self.get_form(request.POST, request.FILES)
		if form.is_valid():
			return self.form_valid(form)
		else:
			return self.form_invalid(form)

	def form_valid(self, form):
		form.instance.user = self.request.user
		form.instance.topic = self.object
		form.instance.ip_address = self.request.META['REMOTE_ADDR']
		form.save()
		return super(TopicDetailView, self).form_valid(form)

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
		return context

	def get(self, request, * args, ** kwargs):
		if not self.get_object().user == request.user:
			return HttpResponseForbidden()

		return super(TopicUpdateView, self).get(request)

	def post(self, request, * args, ** kwargs):
		if not self.get_object().user == request.user:
			return HttpResponseForbidden()

		return super(TopicUpdateView, self).post(request)

	def form_valid(self, form):
		topic = form.save(commit=False)
		topic.date = timezone.now()
		topic.save()
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