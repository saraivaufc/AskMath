from django.utils.translation import ugettext_lazy as _
from django.views.generic.list import ListView
from django.conf import settings

from ..models import Category

class CategoryListView(ListView):
	template_name = 'forum/category/list.html'
	model = Category
	paginate_by = settings.PAGINATE_BY

	def get_queryset(self):
		"""Return the last published issues."""
		return Category.objects.filter(status='p')