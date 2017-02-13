# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms

from ..models import Introduction

class IntroductionForm(forms.ModelForm):
	class Meta:
		model = Introduction
		fields = ['text', ]