# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django import forms

import hashlib

from ..models import User

class UserCreationForm(forms.ModelForm):
	terms = forms.BooleanField(label=_('Terms and Conditions'), widget=forms.CheckboxInput(), help_text=_("Clicking here, you agree to the Terms and Conditions set out by this site, including our Cookie Use."))
	class Meta:
		model = User
		fields = ["first_name", "last_name", "email", "password", "terms"]
		widgets = {
			'password': forms.PasswordInput(attrs={}),
		}

class UserChangeForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ["first_name", "last_name", "profile_image"]

	def clean_profile_image(self):
		profile_image = self.cleaned_data["profile_image"]
		try:
			if profile_image:
				hash = hashlib.md5(profile_image.read()).hexdigest()
				if profile_image.name.find(hash) == -1:
					profile_image.name = "".join((hash, ".", profile_image.name.split(".")[-1]))
		except Exception as e:
			raise forms.ValidationError(e)
		return profile_image