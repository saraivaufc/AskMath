from django.utils.translation import ugettext_lazy as _
from django.views.generic.list import ListView

from ..models import SocialNetwork

class ContactListView(ListView):
	template_name = 'base/contact.html'
	model = SocialNetwork

	def get_queryset(self):
		return SocialNetwork.objects.all()