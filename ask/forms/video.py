# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms

from ..models import Video

class VideoForm(forms.ModelForm):
	class Meta:
		model = Video
		fields = ['position', 'title', 'description', 'url',]