"""
	base URL Configuration
"""
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.views.generic.base import TemplateView
from django.contrib.flatpages import views
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from django_js_reverse.views import urls_js
from django.views.decorators.cache import cache_page
from django.views.i18n import JavaScriptCatalog

from django.views.static import serve

from django.contrib import sitemaps
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import GenericSitemap

from django.contrib.flatpages import views
from django.contrib.flatpages.sitemaps import FlatPageSitemap

from ..sitemap import (issues, lessons, topics)
from ..views.timezone import timezone_view

urlpatterns = (
	url(_(r'^about/$'), views.flatpage, {'url': _(u'/about/')}, name='about'),
	url(_(r'^terms/$'), views.flatpage, {'url': _(u'/terms/')}, name='terms'),
	url(_(r'^privacy/$'), views.flatpage, {'url': _(u'/privacy/')}, name='privacy'),
	
	url(_(r'^report/'), include('base.urls.report')),
	url(_(r'^credits$'), TemplateView.as_view(template_name="base/credits.html"), name='credits'),	
)

urlpatterns += (
	#Files serving
	url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT,}),
	url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,}),
	
	#javascript
	url(r'^jsreverse/$', cache_page(3600)(urls_js), name='js_reverse'),
	url(r'^jsi18n/$', JavaScriptCatalog.as_view(packages=['ask', ]), name='javascript-catalog'),
	
	#Internationalization
	url(_(r'^timezone$'), timezone_view, name='timezone'),
	
	#SiteMap	
	url(r'^sitemap\.xml$', sitemap, {'sitemaps': 
			{
			'flatpages': FlatPageSitemap, 
			'issues': GenericSitemap(issues, priority=0.6), 
			'lessons': GenericSitemap(lessons, priority=0.6),
			'topics': GenericSitemap(topics, priority=0.2),
			}
		}, name='django.contrib.sitemaps.views.sitemap'),
)