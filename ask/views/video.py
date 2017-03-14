from django.utils.translation import ugettext_lazy as _
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponseForbidden
from django.conf import settings

from ask.models import Course, Lesson, Video

class VideoListView(ListView):
	template_name = 'ask/video/list.html'
	model = Video
	paginate_by = settings.PAGINATE_BY

	def get_course(self):
		return Course.objects.filter(slug=self.kwargs['course_slug']).first()

	def get_lesson(self):
		return Lesson.objects.filter(slug=self.kwargs['lesson_slug']).first()

	def get_queryset(self):
		"""Return the last published courses."""
		return self.get_lesson().videos.all()

	def get_context_data(self, ** kwargs):
		context = super(VideoListView, self).get_context_data(** kwargs)
		context['course'] = self.get_course()
		context['lesson'] = self.get_lesson()
		return context

class VideoDetailView(DetailView):
	template_name = 'ask/video/detail.html'
	model = Video

	def get_course(self):
		return Course.objects.filter(slug=self.kwargs['course_slug']).first()

	def get_lesson(self):
		return Lesson.objects.filter(slug=self.kwargs['lesson_slug']).first()

	def get_context_data(self, ** kwargs):
		context = super(VideoDetailView, self).get_context_data(** kwargs)
		context['course'] = self.get_course()
		context['lesson'] = self.get_lesson()
		return context