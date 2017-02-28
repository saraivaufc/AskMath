from django.utils.translation import ugettext_lazy as _
from django.conf.urls import url
from .views import IssueList, LessonList

urlpatterns = (
    url(_(r'^issue/$'), IssueList.as_view(), name='api_issue'),
    url(_(r'^lesson/$'), LessonList.as_view(), name='api_lesson'),
)