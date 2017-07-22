# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms

import hashlib

from ..models import Post

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['title', 'description', 'image', 'categories']

	def clean_image(self):
		image = self.cleaned_data["image"]
		try:
			if image and self.is_valid():
				hash = hashlib.md5(image.read()).hexdigest()
				if image.name.find(hash) == -1:
					image.name = "".join((hash, ".", image.name.split(".")[-1]))
		except Exception as e:
			raise forms.ValidationError(e)
		return image