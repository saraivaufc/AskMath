# -*- coding: utf-8 -*-
from __future__ import unicode_literals

def lists_to_list(lists):
	temp = []
	for i in lists:
		temp.extend(i)
	return temp