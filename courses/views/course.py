from django.utils.translation import ugettext_lazy as _
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.detail import SingleObjectMixin
from django.conf import settings

from courses.models import Course

class CourseListView(ListView):
	template_name = 'courses/course/list.html'
	model = Course
	paginate_by = settings.PAGINATE_BY

	def get_queryset(self):
		"""Return the last published courses."""
		return Course.objects.filter(status=Course.PUBLISHED)


class CourseDetailView(SingleObjectMixin, ListView):
	template_name = 'courses/course/detail.html'
	model = Course

	def get(self, request, * args, ** kwargs):
		self.object = self.get_object(queryset=Course.objects.all())
		if (self.object.status == Course.PUBLISHED) or request.user.is_staff:
			return super(CourseDetailView, self).get(request, * args, ** kwargs)
		else:
			return HttpResponseForbidden()

	def get_context_data(self, ** kwargs):
		context = super(CourseDetailView, self).get_context_data( ** kwargs)
		context['profile'] = self.object
		return context

	def get_queryset(self):
		return self.object.lessons