from django import forms

from ..models import Topic
from ..utils.constants import Constants

class TopicForm(forms.ModelForm):
	
	class Meta:
		model = Topic
		fields = ['category', 'title',]
		widgets = {
			'title': forms.TextInput(attrs={'onkeyup':'Preview_id_title.Update()', 'title': Constants.HELP_TEXT_LATEX}), 
		}