# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.forms import ModelForm

from ..models import Challenge, Solution

class ChallengeForm(ModelForm):
	class Meta:
		model = Challenge
		fields = ['title', 'description', 'level', 'status']

class SolutionForm(ModelForm):
	class Meta:
		model = Solution
		fields = ['text']