# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView, SingleObjectMixin
from django.conf import settings

from ..models import Category, Post

class PostListView(ListView):
	template_name = 'blog/post/list.html'
	model = Post
	paginate_by = settings.PAGINATE_BY

	def get_context_data(self, ** kwargs):
		context = super(PostListView, self).get_context_data(** kwargs)
		context['categories'] = Category.objects.all()
		return context

class PostByCategoryListView(SingleObjectMixin, ListView):
	template_name = 'blog/post/list.html'
	paginate_by = settings.PAGINATE_BY

	def get(self, request, * args, ** kwargs):
		self.object = self.get_object(queryset=Category.objects.all())
		return super(PostByCategoryListView, self).get(request, * args, ** kwargs)

	def get_context_data(self, ** kwargs):
		context = super(PostByCategoryListView, self).get_context_data(** kwargs)
		context['category'] = self.object
		context['categories'] = Category.objects.all()
		return context

	def get_queryset(self):
		return self.object.post_set.all()


class PostDetailView(DetailView):
	template_name = 'blog/post/detail.html'
	model = Post

	def get_context_data(self, ** kwargs):
		context = super(PostDetailView, self).get_context_data(** kwargs)
		context['categories'] = Category.objects.all()
		return context