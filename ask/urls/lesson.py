from django.conf.urls import include, url
from django.utils.translation import ugettext_lazy as _

from ask.views import LessonListView, LessonDetailView, LessonFinishedView

urlpatterns = [
	url(_(r'^list$'), LessonListView.as_view(), name="lesson_list"),
	url(_(r'^(?P<slug>[-\w]+)$'), LessonDetailView.as_view(), name="lesson_detail"),
	url(_(r'^(?P<slug>[-\w]+)/finished$'), LessonFinishedView.as_view(), name="lesson_finished"),
]