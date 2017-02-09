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

urlpatterns = (
	url(r'^$', RedirectView.as_view(url=reverse_lazy('ask:home'), permanent=False), name='home'),
	url(_(r'^about/$'), views.flatpage, {'url': _(u'/about/')}, name='about'),
	url(_(r'^license/$'), views.flatpage, {'url': _(u'/license/')}, name='license'),
	url(_(r'^terms/$'), views.flatpage, {'url': _(u'/terms/')}, name='terms'),
	url(_(r'^policies/$'), views.flatpage, {'url': _(u'/policies/')}, name='policies'),
	url(_(r'^credits/$'), views.flatpage, {'url': _(u'/credits/')}, name='credits'),
	url(_(r'^contact/'), include('base.urls.contact')),
)

def handler404(request):
	response = render_to_response('base/404.html', {}, context_instance=RequestContext(request))
	response.status_code = 404
	return response


def handler500(request):
	response = render_to_response('base/500.html', {}, context_instance=RequestContext(request))
	response.status_code = 500
	return response
