"""
	askmath URL Configuration
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.views.static import serve
from django_js_reverse.views import urls_js
from django.views.decorators.cache import cache_page
from django.contrib.flatpages import views
from django.contrib.flatpages.sitemaps import FlatPageSitemap
from django.contrib.sitemaps.views import sitemap
from django.views.i18n import JavaScriptCatalog
from django.views.generic.base import TemplateView
from django.utils.translation import ugettext_lazy as _

urlpatterns = i18n_patterns(
	url(_(r'^ask/'), include('ask.urls', namespace="ask", app_name="ask")),
	url(_(r'^authentication/'), include('authentication.urls', namespace="authentication", app_name="authentication")),

	url(r'^admin/', include(admin.site.urls)),
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	url(r'^rosetta/', include('rosetta.urls')),
	url(r'^i18n/', include('django.conf.urls.i18n')),

	url(_(r'^about-us/$'), views.flatpage, {'url': _(u'/about-us/')}, name='about'),
	url(_(r'^license/$'), views.flatpage, {'url': _(u'/license/')}, name='license'),
	url(_(r'^terms/$'), views.flatpage, {'url': _(u'/terms/')}, name='terms'),
	url(_(r'^policies/$'), views.flatpage, {'url': _(u'/policies/')}, name='policies'),
	url(_(r'^contact_us$'), TemplateView.as_view(template_name="contact_us.html"), name="contact_us"),
)

urlpatterns += (
	url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,}),
	url(r'^jsreverse/$', cache_page(3600)(urls_js), name='js_reverse'),
	url(r'^jsi18n/$', JavaScriptCatalog.as_view(packages=['ask', ]), name='javascript-catalog'),
	url(r'^sitemap\.xml$', sitemap, {'sitemaps': {'flatpages': FlatPageSitemap}}, name='django.contrib.sitemaps.views.sitemap'),
)
