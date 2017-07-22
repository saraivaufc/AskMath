from __future__ import unicode_literals

THOUSAND_SEPARATOR = '\xa0'

DATE_FORMAT = 'Y/m/d'
DATE_INPUT_FORMATS = [
	'%Y/%m/%d', #'2016/02/01'
]

TIME_FORMAT = 'H:i:s'
TIME_INPUT_FORMATS = [
	'%H:%M', #'10:34'
	'%H:%M:%S', #'10:34:00'
]

DATETIME_FORMAT = 'Y/m/d H:i:s'
DATETIME_INPUT_FORMATS = [
	'%Y/%m/%d', # '2016/02/01'
	'%Y/%m/%d %H:%M', # '2016/02/01 10:34'
	'%Y/%m/%d %H:%M:%S', # '2016/02/01 10:34:00'
]