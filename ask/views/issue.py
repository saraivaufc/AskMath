from django.utils.translation import ugettext_lazy as _
from django.views.generic.list import ListView
from django.conf import settings

from ask.models import Issue

class IssueListView(ListView):
	template_name = 'ask/issue/list.html'
	model = Issue
	paginate_by = settings.PAGINATE_BY

	def get_queryset(self):
		"""Return the last published issues."""
		return Issue.objects.filter(status='p')