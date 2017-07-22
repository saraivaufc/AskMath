"""
	base URL Configuration
"""
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.views.generic.base import TemplateView
from django.views.generic.base import RedirectView
from django.contrib.flatpages import views
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.core.urlresolvers import reverse_lazy

from django.views.static import serve

from django.contrib.flatpages import views

from base import settings as local_settings
from .views.timezone import timezone_view
from .views import ReportCreateView

urlpatterns = (
	url(_(r'^home$'), RedirectView.as_view(url=local_settings.SITE_HOME), name='home'),
	url(_(r'^about/$'), views.flatpage, {'url': _('/about/')}, name='about'),
	url(_(r'^terms/$'), views.flatpage, {'url': _('/terms/')}, name='terms'),
	url(_(r'^privacy/$'), views.flatpage, {'url': _('/privacy/')}, name='privacy'),
	url(_(r'^contact_us$'), ReportCreateView.as_view(), name="contact_us"),
)

urlpatterns += (
	#Files serving
	url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT,'show_indexes': False}),
	url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, 'show_indexes': False}),
	
	#Internationalization
	url(_(r'^timezone$'), timezone_view, name='timezone'),
)