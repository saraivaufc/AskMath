from django.utils.translation import ugettext_lazy as _
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponseForbidden
from django.conf import settings

from ask.models import Issue, Lesson, Video

class VideoListView(ListView):
	template_name = 'ask/video/list.html'
	model = Video
	paginate_by = settings.PAGINATE_BY

	def get_issue(self):
		return Issue.objects.filter(slug=self.kwargs['issue_slug']).first()

	def get_lesson(self):
		return Lesson.objects.filter(slug=self.kwargs['lesson_slug']).first()

	def get_queryset(self):
		"""Return the last published issues."""
		return self.get_lesson().videos.filter(status='p')

	def get_context_data(self, ** kwargs):
		context = super(VideoListView, self).get_context_data(** kwargs)
		context['issue'] = self.get_issue()
		context['lesson'] = self.get_lesson()
		return context

class VideoDetailView(DetailView):
	template_name = 'ask/video/detail.html'
	model = Video

	def get_issue(self):
		return Issue.objects.filter(slug=self.kwargs['issue_slug']).first()

	def get_lesson(self):
		return Lesson.objects.filter(slug=self.kwargs['lesson_slug']).first()

	def get_context_data(self, ** kwargs):
		context = super(VideoDetailView, self).get_context_data(** kwargs)
		context['issue'] = self.get_issue()
		context['lesson'] = self.get_lesson()
		return context

	def get(self, request, * args, ** kwargs):
		if not self.get_object().status == 'p':
			return HttpResponseForbidden()
		return super(VideoDetailView, self).get(request)
