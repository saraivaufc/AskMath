"""
	askmath URL Configuration
"""
from django.utils.translation import ugettext_lazy as _
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns

from django.core.urlresolvers import reverse_lazy
from django.views.generic.base import RedirectView

#from django.contrib import admin
from partners_admin.admin import partners_admin

urlpatterns = i18n_patterns(
	url(r'^', include('base.urls', namespace="base", app_name="base")),
	url(r'^', include('ask.urls', namespace="ask", app_name="ask")),
	url(r'^', include('authentication.urls', namespace="authentication", app_name="authentication")),
	url(r'^', include('forum.urls', namespace="forum", app_name="forum")),
	
	url(r'^admin/', include(partners_admin.urls)),
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^rosetta/', include('rosetta.urls')),
	url(r'^i18n/', include('django.conf.urls.i18n')),
	prefix_default_language=False, 
)

from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.views.defaults import page_not_found

#Bad request
def handler400(request):
	return render(request,  template_name='base/handlers/400.html')
	response.status_code = 400
	return response

#Permission denied
def handler403(request):
	return render(request,  template_name='base/handlers/403.html')
	response.status_code = 403
	return response

#Page not found
def handler404(request):
	return render(request,  template_name='base/handlers/404.html')
	response.status_code = 404
	return response

#Server error
def handler500(request):
	return render(request,  template_name='base/handlers/500.html')
	response.status_code = 500
	return response