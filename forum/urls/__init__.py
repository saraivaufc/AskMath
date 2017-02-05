from django.conf.urls import include, url
from django.utils.translation import ugettext_lazy as _

urlpatterns = [
	url(_(r'^categories/'), include('forum.urls.category')),
	url(_(r'^categories/(?P<category_slug>[-\w]+)/topics/'), include('forum.urls.topic')),
]