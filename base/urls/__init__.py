"""
	base URL Configuration
"""
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib.flatpages import views
from django.views.generic.base import TemplateView, RedirectView
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render_to_response
from django.template import RequestContext
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

from ..sitemap import (issues, lessons, categories, topics)
from ..views.language import language_config

urlpatterns = (
	url(r'^$', RedirectView.as_view(url=reverse_lazy('ask:home'), permanent=False), name='home'),
	url(_(r'^about/$'), views.flatpage, {'url': _(u'/about/')}, name='about'),
	url(_(r'^license/$'), views.flatpage, {'url': _(u'/license/')}, name='license'),
	url(_(r'^terms/$'), views.flatpage, {'url': _(u'/terms/')}, name='terms'),
	url(_(r'^policies/$'), views.flatpage, {'url': _(u'/policies/')}, name='policies'),
	url(_(r'^credits/$'), views.flatpage, {'url': _(u'/credits/')}, name='credits'),
	url(_(r'^contact/'), include('base.urls.contact')),
)

urlpatterns += (
	#Files serving
	url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT,}),
	url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,}),
	
	#javascript
	url(r'^jsreverse/$', cache_page(3600)(urls_js), name='js_reverse'),
	url(r'^jsi18n/$', JavaScriptCatalog.as_view(packages=['ask', ]), name='javascript-catalog'),
	
	#Internationalization
	url(_(r'^language$'), language_config, name='language'),
	
	#SiteMap	
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

def handler404(request):
	response = render_to_response('base/404.html', {}, context_instance=RequestContext(request))
	response.status_code = 404
	return response


def handler500(request):
	response = render_to_response('base/500.html', {}, context_instance=RequestContext(request))
	response.status_code = 500
	return response
