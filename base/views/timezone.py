from django.utils.translation import ugettext_lazy as _
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponseRedirect
import pytz

def timezone_view(request):
	if request.method == 'POST' and request.POST.has_key('timezone'):
		request.session['django_timezone'] = request.POST['timezone']
		messages.success(request, _("Timezone configured success"))
		return HttpResponseRedirect(request.path)
	return render(request, 'base/timezone.html', {'timezones': pytz.common_timezones})