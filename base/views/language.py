from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponseRedirect
import pytz

from ..utils.constants import Constants

def get_config(request):
	return render(request, 'base/language.html', {'timezones': pytz.common_timezones})

def set_timezone(request):
	if request.method == 'POST' and request.POST.has_key('timezone'):
		request.session['django_timezone'] = request.POST['timezone']
		messages.success(request, Constants.TIMEZONE_SUCCESS_CONFIG)
	return get_config(request)