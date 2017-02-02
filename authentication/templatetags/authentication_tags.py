# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.forms import CheckboxInput, RadioSelect, ClearableFileInput, Select, SelectMultiple, TextInput, PasswordInput, EmailInput, Textarea, NumberInput, DateInput, DateTimeInput, URLInput


from django import template


register = template.Library()


@register.filter(name='is_checkbox')
def is_checkbox(field):
	return field.field.widget.__class__.__name__ == CheckboxInput().__class__.__name__


@register.filter(name='is_radio')
def is_radio(field):
	return field.field.widget.__class__.__name__ == RadioSelect().__class__.__name__


@register.filter(name='is_file')
def is_file(field):
	return field.field.widget.__class__.__name__ == ClearableFileInput().__class__.__name__


@register.filter(name='is_password')
def is_password(field):
	return field.field.widget.__class__.__name__ == PasswordInput().__class__.__name__


@register.filter(name='is_select')
def is_select(field):
	return field.field.widget.__class__.__name__ == Select().__class__.__name__


@register.filter(name='is_select_multiple')
def is_select(field):
	return field.field.widget.__class__.__name__ == SelectMultiple().__class__.__name__


@register.filter(name='is_text')
def is_text(field):
	return field.field.widget.__class__.__name__ == TextInput().__class__.__name__


@register.filter(name='is_email')
def is_email(field):
	return field.field.widget.__class__.__name__ == EmailInput().__class__.__name__


@register.filter(name='is_textarea')
def is_textarea(field):
	return field.field.widget.__class__.__name__ == Textarea().__class__.__name__


@register.filter(name='is_number')
def is_number(field):
	return field.field.widget.__class__.__name__ == NumberInput().__class__.__name__


@register.filter(name='is_date')
def is_date(field):
	return field.field.widget.__class__.__name__ == DateInput().__class__.__name__


@register.filter(name='is_datetime')
def is_datetime(field):
	return field.field.widget.__class__.__name__ == DateTimeInput().__class__.__name__


@register.filter(name='is_url')
def is_url(field):
	return field.field.widget.__class__.__name__ == URLInput().__class__.__name__