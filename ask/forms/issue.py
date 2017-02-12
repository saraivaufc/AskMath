# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.forms import ModelForm

from ..models import Issue

class IssueForm(ModelForm):
	class Meta:
		model = Issue
		fields = ['name', 'icon', 'status',]
