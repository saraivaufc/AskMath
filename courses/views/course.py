from django.utils.translation import ugettext_lazy as _
from django.views.generic.list import ListView
from django.conf import settings

from courses.models import Course

class CourseListView(ListView):
	template_name = 'courses/course/list.html'
	model = Course
	paginate_by = settings.PAGINATE_BY

	def get_queryset(self):
		"""Return the last published courses."""
		return Course.objects.filter(status=Course.PUBLISHED)