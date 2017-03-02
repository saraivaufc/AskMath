# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _

from django import forms

from ..models import User

class UserForm(forms.ModelForm):
	terms = forms.BooleanField(label=_('Agree the Terms and Conditions'), widget=forms.CheckboxInput(), help_text=_("Clicking here, you agree to the Terms and Conditions set out by this site, including our Cookie Use."))
	class Meta:
		model = User
		fields = ["first_name", "last_name", "username", "email", "password", "terms"]