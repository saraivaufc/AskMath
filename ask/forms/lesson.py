from django.forms import ModelForm

from ..models import Lesson

class LessonForm(ModelForm):
	class Meta:
		model = Lesson
		fields = ['name', 'description', 'status', 'issues', 'requirements', 'questions']
