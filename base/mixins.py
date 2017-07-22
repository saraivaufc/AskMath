from django.http import JsonResponse

class AjaxableResponseMixin(object):
	def form_invalid(self, form):
		response = super(AjaxableResponseMixin, self).form_invalid(form)
		if self.request.is_ajax() or self.request.POST['is_popup'] == "true":
			data = {
				'status': 'error',
				'errors':form.errors,
			}
			return JsonResponse(data)
		else:
			return response
	def form_valid(self, form):
		response = super(AjaxableResponseMixin, self).form_valid(form)
		if self.request.is_ajax() or self.request.POST['is_popup'] == "true":
			data = {
				'status': 'success',
				'pk': self.object.pk,
				'representation': str(self.object),
			}
			return JsonResponse(data)
		else:
			return response

	def get_context_data(self, ** kwargs):
		context = super(AjaxableResponseMixin, self).get_context_data(** kwargs)
		context['model'] = self.model
		context['is_popup'] = True
		return context