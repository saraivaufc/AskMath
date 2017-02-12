"""
	askmath URL Configuration
"""
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns

from django.utils.translation import ugettext_lazy as _

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
)