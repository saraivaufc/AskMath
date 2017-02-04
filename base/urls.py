"""
	base URL Configuration
"""
from django.conf.urls import url
from django.conf.urls.i18n import i18n_patterns
from django.contrib.flatpages import views
from django.views.generic.base import TemplateView, RedirectView
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext_lazy as _

urlpatterns = (
	url(r'^$', RedirectView.as_view(url=reverse_lazy('ask:home'), permanent=False), name='home'),
	url(_(r'^about-us/$'), views.flatpage, {'url': _(u'/about-us/')}, name='about'),
	url(_(r'^license/$'), views.flatpage, {'url': _(u'/license/')}, name='license'),
	url(_(r'^terms/$'), views.flatpage, {'url': _(u'/terms/')}, name='terms'),
	url(_(r'^policies/$'), views.flatpage, {'url': _(u'/policies/')}, name='policies'),
	url(_(r'^credits/$'), views.flatpage, {'url': _(u'/credits/')}, name='credits'),
	url(_(r'^contact_us$'), TemplateView.as_view(template_name="base/contact_us.html"), name="contact_us"),
)