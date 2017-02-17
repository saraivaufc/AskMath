from django.conf.urls import include, url
from django.utils.translation import ugettext_lazy as _

urlpatterns = [
	url(_(r'^forum/'), include('forum.urls.topic')),
	url(_(r'^forum/(?P<topic_slug>[-\w]+)/'), include('forum.urls.comment')),
]