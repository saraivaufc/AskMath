# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.forms import ModelForm

from ..models import Course

class CourseForm(ModelForm):
	class Meta:
		model = Course
		fields = ['name', 'icon', 'status',]
