from django.conf.urls import include, url
from django.views.generic.base import TemplateView
from django.views.generic.base import RedirectView
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext_lazy as _

urlpatterns = [
	url(r'^$', RedirectView.as_view(url=reverse_lazy('ask:home'), permanent=False)),
	url(_(r'^index$'), TemplateView.as_view(template_name="ask/index.html"), name="home"),

	url(_(r'^issue/'), include('ask.urls.issue')),
	url(_(r'^issue/(?P<issue_slug>[-\w]+)/lesson/'), include('ask.urls.lesson')),
	url(_(r'^issue/(?P<issue_slug>[-\w]+)/lesson/(?P<lesson_slug>[-\w]+)/question/'), include('ask.urls.question')),
]