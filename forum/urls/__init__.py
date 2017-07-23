from django.conf.urls import include, url
from django.utils.translation import ugettext_lazy as _

urlpatterns = [
	url(_(r'^topic/'), include('forum.urls.topic')),
	url(_(r'^topic/(?P<topic_slug>[-\w]+)/comment/'), include('forum.urls.comment')),
]