#!/usr/bin/env python
import os, sys, json

f = sys.argv[1]
f_json = json.loads(open(f).read())
for page in f_json:
	template = page['fields']['content']
	page['fields']['content'] = open(template, "r").read()

new_file = open(sys.argv[1].replace(".json", "_output.json"), "w")
new_file.write(json.dumps(f_json, indent=4)) 