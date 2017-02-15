from django import forms
from django.utils.translation import ugettext_lazy as _

from ..models import Comment
from ..utils.constants import Constants

class CommentForm(forms.ModelForm):
	
	class Meta:
		model = Comment
		fields = ['text',]
		widgets = {
			'text': forms.Textarea(attrs={'rows': 2, 'onkeyup':'Preview_id_text.Update()', 'title': Constants.HELP_TEXT_LATEX}), 
		}