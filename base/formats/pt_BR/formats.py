from __future__ import unicode_literals

THOUSAND_SEPARATOR = '\xa0'

DATE_FORMAT = 'd/m/Y'
DATE_INPUT_FORMATS = [
	'%d/%m/%Y', #'01/02/2016'
]

TIME_FORMAT = 'H:i:s'
TIME_INPUT_FORMATS = [
	'%H:%M', #'10:34'
	'%H:%M:%S', #'10:34:00'
]

DATETIME_FORMAT = 'd/m/Y H:i:s'
DATETIME_INPUT_FORMATS = [
	'%d/%m/%Y', # '01/02/2016'
	'%d/%m/%Y %H:%M', # '01/02/2016 10:34'
	'%d/%m/%Y %H:%M:%S', # '01/02/2016 10:34:00'
]