from django.contrib import messages

from .utils.constants import Constants

class SortableAction(object):
	def sort_fields(self, request, model, count):
		if request.method == 'POST':
			for i in range(1, count+1):
				if request.POST.has_key('result_{}'.format(i)):
					result = request.POST['result_{}'.format(i)]
					model.objects.filter(pk=result).update(position=i)

			messages.success(request, Constants.OBJECTS_ORDERED_SUCCESS)
			return True
		else:
			messages.error(request, Constants.OBJECTS_ORDERED_ERROR)
			return False

	def get_context(self, request):
		opts = self.model._meta
		context = dict(
			self.admin_site.each_context(request),
			opts=opts,
			has_change_permission=True,
		)
		return context