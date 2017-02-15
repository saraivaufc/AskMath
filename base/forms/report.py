# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms

from ..models import Report

class ReportForm(forms.ModelForm):
	class Meta:
		model = Report
		fields = ['page', 'text']