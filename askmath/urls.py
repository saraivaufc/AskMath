"""
	askmath URL Configuration
"""
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings

from django.views.static import serve
from django_js_reverse.views import urls_js
from django.views.decorators.cache import cache_page
from django.views.i18n import JavaScriptCatalog
from django.views.generic.base import TemplateView, RedirectView
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext_lazy as _

from django.contrib.flatpages import views
from django.contrib.flatpages.sitemaps import FlatPageSitemap

from django.contrib import sitemaps
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import GenericSitemap

from django.views.decorators.cache import cache_page

#from django.contrib import admin
from partners_admin.admin import partners_admin

from .sitemap import (issues, lessons,
					  categories, topics)

print FlatPageSitemap

urlpatterns = i18n_patterns(
	url(r'^', include('ask.urls', namespace="ask", app_name="ask")),
	url(r'^base/', include('base.urls', namespace="base", app_name="base")),
	url(r'^authentication/', include('authentication.urls', namespace="authentication", app_name="authentication")),
	url(r'^forum/', include('forum.urls', namespace="forum", app_name="forum")),
	
	url(r'^admin/', include(partners_admin.urls)),
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^rosetta/', include('rosetta.urls')),
	url(r'^i18n/', include('django.conf.urls.i18n')),

	url(r'^sitemap\.xml$', sitemap, {'sitemaps': 
			{
			'flatpages': FlatPageSitemap, 
			'issues': GenericSitemap(issues, priority=0.6), 
			'lessons': GenericSitemap(lessons, priority=0.6),
			'categories': GenericSitemap(categories, priority=0.6),
			'topics': GenericSitemap(topics, priority=0.2),
			}
		}, name='django.contrib.sitemaps.views.sitemap'),	
)

urlpatterns += (
	url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT,}),
	url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,}),
	url(r'^jsreverse/$', cache_page(3600)(urls_js), name='js_reverse'),
	url(r'^jsi18n/$', JavaScriptCatalog.as_view(packages=['ask', ]), name='javascript-catalog'),
)