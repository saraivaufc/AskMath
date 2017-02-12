# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.forms import ModelForm

from ..models import Lesson

class LessonForm(ModelForm):
	class Meta:
		model = Lesson
		fields = ['name', 'description', 'status', 'issues', 'requirements', 'questions', 'videos',]
