# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template
from django.http import QueryDict


register = template.Library()

@register.filter(name='range')
def range_(number):
	return range(number)

@register.filter(name='remove')
def remove(value, arg):
	"""Removes value of arg from the given value"""
	if type(value) == type(QueryDict()) and value.get(arg):
		value_copy = value.copy()
		del value_copy[arg]
		value = value_copy
	if type(value) == type({}) and value.get(arg):
		del value[arg]
	if type(value) == type([]) and arg in value:
		value.remove(arg)
	return value