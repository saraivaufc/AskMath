# -*- coding: utf-8 -*-

import os
import glob
import re

TEXT = "issue"
NEW_TEXT = "course"
FILE_TYPES = ['(.)\.py', ]

rexs = []
for i in FILE_TYPES:
	rexs.append(re.compile(i))



BASE_DIR = os.getcwd() + '/'
SELF = BASE_DIR + "replace.py"

def find(path='.'):
	for item in os.listdir(path):
		fn = os.path.normpath(os.path.join(path, item))
		
		if os.path.isdir(fn):
			for f in find(fn):
				yield f
		else:
			passer = False
			for rex in rexs:
				if bool(rex.search(fn)):
					passer = True
			if not passer:
				continue
			yield fn

def replace(f, text, new_text):
	temp_file = file(f, "r")
	text_replaced = temp_file.read()
	temp_file.close()
	
	text_replaced = text_replaced.replace(text, new_text)
	
	temp_file = file(f, "w")
	temp_file.write(text_replaced)
	temp_file.close()
	
for fn in find():
	fn = BASE_DIR + fn
	if not fn == SELF:
		print "Ok"
		replace(fn,TEXT, NEW_TEXT)
	else:
		print "Erro"
