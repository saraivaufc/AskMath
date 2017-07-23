from django.conf.urls import include, url
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.decorators import login_required

from forum.views import TopicListView, TopicDetailView, TopicCreateView, TopicUpdateView, TopicDeleteView

urlpatterns = [
	url(r'^list$', TopicListView.as_view(), name="topic_list"),
	url(r'^add$', login_required(TopicCreateView.as_view()), name="topic_add"),
	url(r'^(?P<slug>[-\w]+)/detail$', login_required(TopicDetailView.as_view()), name="topic_detail"),
	url(r'^(?P<slug>[-\w]+)/update$', login_required(TopicUpdateView.as_view()), name="topic_update"),
	url(r'^(?P<slug>[-\w]+)/delete$', login_required(TopicDeleteView.as_view()), name="topic_delete"),
]