from django.forms import ModelForm

from ..models import Choice

class ChoiceForm(ModelForm):
	class Meta:
		model = Choice
		fields = ['text','is_correct',]
