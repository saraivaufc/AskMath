# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.forms import ModelForm

from ..models import Category

class CategoryForm(ModelForm):
	class Meta:
		model = Category
		fields = ['name',]