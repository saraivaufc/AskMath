from django.conf.urls import include, url
from django.utils.translation import ugettext_lazy as _

urlpatterns = [
	url(_(r'^forum/categories/'), include('forum.urls.category')),
	url(_(r'^forum/categories/(?P<category_slug>[-\w]+)/topics/'), include('forum.urls.topic')),
	url(_(r'^forum/categories/(?P<category_slug>[-\w]+)/topics/(?P<topic_slug>[-\w]+)/comments/'), include('forum.urls.comment')),
]