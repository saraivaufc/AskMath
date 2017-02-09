from django.conf.urls import include, url
from django.views.generic.base import TemplateView
from django.views.generic.base import RedirectView
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext_lazy as _

urlpatterns = [
	url(r'^$', RedirectView.as_view(url=reverse_lazy('partners_admin:home'), permanent=False)),
	url(_(r'^index$'), TemplateView.as_view(template_name="partners_admin/index.html"), name="home"),
]

def partners_admin_urls(*args):
    return [
        url(r'', include(urlpatterns)),
    ]